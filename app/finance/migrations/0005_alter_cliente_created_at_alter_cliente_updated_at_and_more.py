# Generated by Django 5.0.2 on 2024-04-27 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_alter_cliente_created_at_alter_cliente_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 57, 32, 725025)),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 57, 32, 725025)),
        ),
        migrations.AlterField(
            model_name='clienteproducto',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 57, 32, 725025)),
        ),
        migrations.AlterField(
            model_name='clienteproducto',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 57, 32, 725025)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 57, 32, 725025)),
        ),
        migrations.AlterField(
            model_name='producto',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 57, 32, 725025)),
        ),
        migrations.AlterField(
            model_name='tipo_transaccion',
            name='abreviatura',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='tipo_transaccion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 57, 32, 725025)),
        ),
        migrations.AlterField(
            model_name='tipo_transaccion',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='tipo_transaccion',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 57, 32, 725025)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 57, 32, 725025)),
        ),
        migrations.AlterField(
            model_name='transaccion',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 4, 27, 16, 57, 32, 725025)),
        ),
    ]
