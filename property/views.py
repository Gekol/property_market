from datetime import date

from django.contrib.auth.models import User
from django.views.generic import TemplateView, View
from . import models
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login

import re


class MainView(TemplateView):
    template_name = "index.html"


class PropertiesView(View):
    def get(self, request):
        properties = models.Property.objects.filter(status="waiting")
        return render(request, "properties.html", {"properties": properties, "users": models.User.objects.all()})

    def post(self, request):
        models.Property.objects.create(description=request.POST["description"], type=request.POST["type"],
                                       address=request.POST["address"], purchase_price=request.POST["purchase_price"],
                                       rent_price=request.POST["rent_price"], owner_id=request.POST["owner"],
                                       rooms_number=request.POST["rooms_number"])
        properties = models.Property.objects.all()
        return render(request, "properties.html", {"properties": properties, "users": models.User.objects.all()})


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class LogInView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return redirect("/properties")
        else:
            return redirect("/log_in")


class MakeOrder(View):
    def get(self, request, id):
        models.Order.objects.create(user_id=request.user.id, property_id=id, status='new',
                                    type=request.path.split('/')[3], date=date.today())
        property = models.Property.objects.get(id=id)
        property.status = "in_progress"
        property.save()
        return redirect('/properties')


class OrderView(View):
    def get(self, request):
        if request.user.is_staff:
            return render(request, "orders.html", {"orders": models.Order.objects.all()})
        return render(request, "orders.html", {"orders": models.Order.objects.filter(user_id=request.user.id)})


class RegisterView(View):
    def get(self, request):
        return render(request, "register.html")

    def __validate_password(self, password) -> str:
        if len(password) < 8:
            return "Password must be at least 8 symbols long!"
        elif not re.search("[a-z]", password):
            return "Password must contain at least one lowercase letter!"
        elif not re.search("[A-Z]", password):
            return "Password must contain at least one uppercase letter!"
        elif not re.search("[0-9]", password):
            return "Password must contain at least one digit!"
        else:
            return ""

    def post(self, request):
        username = request.POST["username"]
        is_valid = True
        errors = {}
        try:
            if User.objects.get(username__contains=username) is not None:
                is_valid = False
                errors["username_error"] = "Username is taken!!!"
        except:
            pass
        email = request.POST["email"]
        try:
            if User.objects.get(email__contains=email) is not None:
                is_valid = False
                errors["email_error"] = "Email is taken!!!"
        except:
            pass
        password = request.POST["password"]
        validation_result = self.__validate_password(password)
        if validation_result != "":
            is_valid = False
            errors["validation_error"] = validation_result
        confirm_password = request.POST["confirm_password"]
        if password != confirm_password:
            is_valid = False
            errors["confirm_password_error"] = "Passwords don't match!!!"
        if not is_valid:
            return render(request, 'register.html', errors)
        user = User.objects.create_user(username=username, password=password, email=email,
                                        first_name=request.POST["first_name"], last_name=request.POST["last_name"])
        authenticate(user)
        return redirect('/properties')


class ChangeOrderStatusView(View):
    def get(self, request, id):
        order = models.Order.objects.get(id=id)
        order.status = 'in_progress' if 'in_progress' in request.path else 'done'
        order.save()
        return redirect('/orders')
