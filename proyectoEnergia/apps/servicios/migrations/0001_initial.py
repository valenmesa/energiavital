# Generated by Django 4.2.1 on 2023-06-20 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='servicios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_Servicio', models.CharField(max_length=100)),
                ('Descripcion_Servicio', models.TextField()),
                ('Valor_Servicio', models.BigIntegerField()),
            ],
        ),
    ]
