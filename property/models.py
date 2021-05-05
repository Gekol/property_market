from django.contrib.auth.models import User
from django.db import models


class Property(models.Model):
    type = models.CharField(max_length=100, choices=[('house', 'House'),
                                                     ('apartments', 'Apartments')])
    description = models.TextField(null=True)
    district = models.CharField(max_length=100, null=False, default='Sobornyi')
    address = models.CharField(max_length=100, null=False, unique=True)
    purchase_price = models.DecimalField(decimal_places=2, max_digits=10, null=False)
    rent_price = models.DecimalField(decimal_places=2, max_digits=10, null=False)
    rooms_number = models.IntegerField(null=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=100, default='waiting',
                              choices=[('in_progress', 'In progress'), ('waiting', 'Waiting for orders')])

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.address


class Order(models.Model):
    date = models.DateField(null=False)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100, choices=[('purchase', 'Purchase'),
                                                     ('rent', 'Rent')])
    status = models.CharField(max_length=100, choices=[('new', 'New'),
                                                       ('in_progress', 'In progress'),
                                                       ('done', 'Done')
                                                       ])

    def __str__(self):
        return self.user.username + " " + self.property.address + " " + str(self.date)
