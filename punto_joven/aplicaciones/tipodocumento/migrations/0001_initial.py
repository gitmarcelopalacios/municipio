# Generated by Django 4.0.4 on 2022-05-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=' ', max_length=250, verbose_name='Tipo de documento')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]