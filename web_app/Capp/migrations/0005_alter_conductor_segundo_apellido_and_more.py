# Generated by Django 4.0.3 on 2022-03-30 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Capp', '0004_alter_conductor_segundo_apellido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conductor',
            name='segundo_apellido',
            field=models.CharField(help_text='Introduzca el 2do Apellido', max_length=50),
        ),
        migrations.AlterField(
            model_name='conductor',
            name='segundo_nombre',
            field=models.CharField(help_text='Introduzca el 2do Nombre', max_length=50),
        ),
    ]
