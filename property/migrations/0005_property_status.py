# Generated by Django 3.2 on 2021-05-04 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_property_district'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('in_progress', 'In progress'), ('waiting', 'Waiting for orders')], default='in_progress', max_length=100),
        ),
    ]
