# Generated by Django 4.0.4 on 2022-05-04 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='domicilio_cliente',
            field=models.CharField(default=' ', max_length=250, verbose_name='Domicilio'),
        ),
    ]
