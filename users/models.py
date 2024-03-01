from django.db import models
from django.views.generic import DetailView

from jobs.models import JobModel


class FrontendUsersModel(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    telegram_link = models.URLField()
    part_link = models.URLField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'




class BackendUsersModel(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    telegram_link = models.URLField()
    part_link = models.URLField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



class TelegramUsersModel(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    telegram_link = models.URLField()
    part_link = models.URLField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



class SmmUsersModel(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    telegram_link = models.URLField()
    part_link = models.URLField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



class GraphicDesignerUsersModel(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    telegram_link = models.URLField()
    part_link = models.URLField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'



class MobilografUsersModel(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    telegram_link = models.URLField()
    part_link = models.URLField()

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


