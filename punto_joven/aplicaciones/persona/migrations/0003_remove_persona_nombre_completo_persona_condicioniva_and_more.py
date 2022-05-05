# Generated by Django 4.0.4 on 2022-05-05 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('condicioniva', '0001_initial'),
        ('tipodocumento', '0001_initial'),
        ('persona', '0002_alter_persona_nombre_completo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='nombre_completo',
        ),
        migrations.AddField(
            model_name='persona',
            name='condicioniva',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='condicioniva.condicioniva'),
        ),
        migrations.AddField(
            model_name='persona',
            name='dom',
            field=models.CharField(default=' ', max_length=250, verbose_name='Domicilio'),
        ),
        migrations.AddField(
            model_name='persona',
            name='name',
            field=models.CharField(default=' ', max_length=250, verbose_name='Alumno'),
        ),
        migrations.AddField(
            model_name='persona',
            name='numconiva',
            field=models.CharField(default=' ', max_length=20, verbose_name='Número de CUIT'),
        ),
        migrations.AddField(
            model_name='persona',
            name='numdoc',
            field=models.CharField(default=' ', max_length=15, verbose_name='Número de documento'),
        ),
        migrations.AddField(
            model_name='persona',
            name='tipodocumento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tipodocumento.tipodocumento'),
        ),
    ]