# Generated by Django 4.0.4 on 2022-05-05 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuenta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuenta',
            options={'ordering': ['name'], 'verbose_name': 'Cuenta Contable', 'verbose_name_plural': 'Cuentas Contables'},
        ),
    ]