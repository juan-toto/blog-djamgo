# Generated by Django 5.0.4 on 2024-06-03 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='sobre_mi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=350, verbose_name='descripcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificacion')),
            ],
            options={
                'verbose_name': 'hacerca',
                'verbose_name_plural': 'hacerca de',
                'ordering': ['-created'],
            },
        ),
        migrations.AlterField(
            model_name='categoria',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='etiqueta',
            name='activo',
            field=models.BooleanField(default=True, verbose_name='Activo'),
        ),
        migrations.AlterField(
            model_name='etiqueta',
            name='nombre',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nombre'),
        ),
    ]
