# Generated by Django 3.2 on 2021-05-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_auto_20210504_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='district',
            field=models.CharField(default='Sobornyi', max_length=100),
        ),
    ]
