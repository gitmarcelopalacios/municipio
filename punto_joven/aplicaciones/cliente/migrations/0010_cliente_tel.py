# Generated by Django 4.0.4 on 2022-05-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0009_alter_cliente_dom_alter_cliente_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='tel',
            field=models.CharField(default=' ', max_length=250, verbose_name='Teléfono'),
        ),
    ]
