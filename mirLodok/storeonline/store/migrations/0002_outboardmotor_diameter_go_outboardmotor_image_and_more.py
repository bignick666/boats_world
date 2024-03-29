# Generated by Django 4.2.7 on 2023-12-09 09:50

from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='outboardmotor',
            name='diameter_go',
            field=models.CharField(default=0.8695652173913043, max_length=100, verbose_name='Диаметр цилиндра/ход поршня'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outboardmotor',
            name='image',
            field=models.ImageField(default=23, upload_to=store.models.upload_path_handler),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='outboardmotor',
            name='launch_system',
            field=models.CharField(choices=[('Ручной запуск', 'Ручной запуск'), ('Электрический запуск', 'Электрический запуск')], default=('Ручной запуск', 'Ручной запуск'), max_length=30, verbose_name='Тип запуска'),
        ),
    ]
