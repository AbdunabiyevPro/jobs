from django.db import models
from django.views.generic import DetailView

from jobs.models import JobModel


class UsersModel(models.Model):
    name = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    job = models.ForeignKey(JobModel, related_name='UsersModel', on_delete=models.CASCADE, null=True, blank=True)
    telegram_link = models.URLField()
    part_link = models.URLField()




    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


class VerificationCodeModel(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4,unique=True)
    status = models.BooleanField(default=False)
    send_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Code'
        verbose_name_plural = 'Codes'



class JobDetailView(DetailView):
    model = JobModel
    template_name = 'telegram-bot.html'
    context_object_name = 'UsersModel'

