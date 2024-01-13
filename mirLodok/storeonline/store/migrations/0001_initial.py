# Generated by Django 4.2.7 on 2023-12-03 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Адрес')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OutboardMotor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=100, verbose_name='Модель мотора')),
                ('type', models.CharField(choices=[('TS', 'Two-Stroked'), ('FS', 'Four-Stroked')], default=('TS', 'Two-Stroked'), max_length=5, verbose_name='Тип мотора')),
                ('volume', models.PositiveSmallIntegerField(verbose_name='Объем двигателя куб.см')),
                ('max_power', models.FloatField(verbose_name='Мощность')),
                ('turnovers', models.IntegerField(verbose_name='Обороты в минуту')),
                ('weight', models.PositiveSmallIntegerField(verbose_name='Вес')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='motor', to='store.group')),
            ],
        ),
    ]