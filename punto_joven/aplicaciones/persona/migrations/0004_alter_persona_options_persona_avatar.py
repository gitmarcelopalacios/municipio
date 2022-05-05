# Generated by Django 4.0.4 on 2022-05-05 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_remove_persona_nombre_completo_persona_condicioniva_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='persona',
            options={'verbose_name': 'Alumno', 'verbose_name_plural': 'Alumnos'},
        ),
        migrations.AddField(
            model_name='persona',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='fotoalumno'),
        ),
    ]
