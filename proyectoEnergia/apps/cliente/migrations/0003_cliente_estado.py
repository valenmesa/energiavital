# Generated by Django 4.2.1 on 2023-09-04 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_alter_cliente_direccion_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]
