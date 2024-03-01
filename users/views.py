import random
from urllib import request
from datetime import datetime, timedelta

import pytz

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import *
from users.forms import *
from conf.settings import *


def home_pages_view(request):
    job = JobModel.objects.all()
    context = {
        'job': job
    }
    return render(request, 'index.html', context=context)


def xizmatlar_view(request):
    return render(request, 'service.html')



def front_register_view(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            return render(request, 'front_register.html')
        else:
            text = form.errors
            return HttpResponse(text)
    else:
        return render(request, 'front_register.html')


def frontend_view(request):
    frontend = FrontendUsersModel.objects.all()
    context = {
        'frontend': frontend
    }
    return render(request, 'frontend.html', context=context)




def backend_register_view(request):
    if request.method == 'POST':
        form = BacRegistrationForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            return render(request, 'backend_register.html')
        else:
            text = form.errors
            return HttpResponse(text)
    else:
        return render(request, 'backend_register.html')



def backend_view(request):
    backend = BackendUsersModel.objects.all()
    context = {
        'backend': backend
    }
    return render(request, 'backend.html', context=context)





def telegram_register_view(request):
    if request.method == 'POST':
        form = TelegramRegistrationForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            return render(request, 'telegram-bot-register.html')
        else:
            text = form.errors
            return HttpResponse(text)
    else:
        return render(request, 'telegram-bot-register.html')



def telegram_view(request):
    telegram = TelegramUsersModel.objects.all()
    context = {
        'telegram': telegram
    }
    return render(request, 'telegram-bot.html', context=context)







def smm_register_view(request):
    if request.method == 'POST':
        form = TelegramRegistrationForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            return render(request, 'smm_register.html')
        else:
            text = form.errors
            return HttpResponse(text)
    else:
        return render(request, 'smm_register.html')



def smm_view(request):
    smm = SmmUsersModel.objects.all()
    context = {
        'smm': smm
    }
    return render(request, 'smm.html', context=context)


















