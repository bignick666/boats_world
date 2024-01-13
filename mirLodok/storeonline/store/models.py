from django.db import models


def upload_path_handler(instance, filename):
    return "{group}/{type}/{model}/{file}".format(group=instance.group,
                                                  type=instance.type,
                                                  model=instance.model,
                                                  file=filename)


class Group(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField(verbose_name='Адрес', unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class OutboardMotor(models.Model):
    type_choices = [
        ('TS', 'Two-Stroked'),
        ('FS', 'Four-Stroked'),
    ]
    type_launch_system = [
        ('Ручной запуск', 'Ручной запуск'),
        ('Электрический запуск', 'Электрический запуск')
    ]
    model = models.CharField(max_length=100, verbose_name='Модель мотора')
    type = models.CharField(max_length=5,
                            default=type_choices[0],
                            choices=type_choices,
                            verbose_name='Тип мотора')
    volume = models.PositiveSmallIntegerField(verbose_name='Объем двигателя куб.см')
    max_power = models.FloatField(verbose_name='Мощность')
    turnovers = models.IntegerField(verbose_name='Обороты в минуту')
    weight = models.PositiveSmallIntegerField(verbose_name='Вес')
    launch_system = models.CharField(max_length=30,
                                     verbose_name='Тип запуска',
                                     default=type_launch_system[0],
                                     choices=type_launch_system)
    diameter_go = models.CharField(max_length=100, verbose_name='Диаметр цилиндра/ход поршня')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='motor')
    image = models.ImageField(upload_to=upload_path_handler)

    def __str__(self):
        return f'{self.group} {self.model}'

    class Meta:
        verbose_name = 'Мотор'
        verbose_name_plural = 'Моторы'
