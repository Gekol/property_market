# Generated by Django 3.2 on 2021-05-03 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'Properties'},
        ),
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='rent_price',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10),
            preserve_default=False,
        ),
    ]
