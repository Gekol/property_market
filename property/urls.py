from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('properties', views.PropertiesView.as_view()),
    path('log_out', views.LogOutView.as_view()),
    path('log_in', views.LogInView.as_view()),
    path('register', views.RegisterView.as_view()),
    path('properties/purchase/<int:id>', views.MakeOrder.as_view()),
    path('properties/rent/<int:id>', views.MakeOrder.as_view()),
    path('orders', views.OrderView.as_view()),
    path('orders/<int:id>/in_progress', views.ChangeOrderStatusView.as_view()),
    path('orders/<int:id>/done', views.ChangeOrderStatusView.as_view())
]
