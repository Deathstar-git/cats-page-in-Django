from django.db import models


class Cat(models.Model):
    name = models.CharField('Имя', max_length=20)
    age = models.CharField('Возраст', max_length=3)
    color = models.CharField('Цвет', max_length=20)

    def __str__(self):
        return self.name
