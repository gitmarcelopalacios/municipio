# Generated by Django 4.0.4 on 2022-05-05 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0005_alter_cliente_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={},
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='domicilio_cliente',
            new_name='domicilio',
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='cliente',
            new_name='emprendimiento',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='name',
            field=models.CharField(default=' ', max_length=250, verbose_name='Cliente'),
        ),
    ]
