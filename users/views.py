import random
from urllib import request
from datetime import datetime, timedelta

import pytz

from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import *
from users.forms import RegistrationForms
from conf.settings import *


def home_pages_view(request):
    job = JobModel.objects.all()
    context = {
        'job': job
    }
    return render(request, 'index.html', context=context)


def xizmatlar_view(request):
    return render(request, 'service.html')


def users_view(request, pk):
    users = UsersModel.objects.all()
    if pk == 1:
        users = UsersModel.objects.filter(job__title__icontains='telegram')

    context = {
        'users': users
    }
    return render(request, 'telegram-bot.html', context=context)


def webcite_view(request, pk):
    users = UsersModel.objects.all()
    if pk == 2:
        users = UsersModel.objects.filter(job__title__icontains='veb')

        context = {
            'users': users
        }
        return render(request, 'veb.html', context=context)


def send_activation_email(email):
    subject = "Activation code"
    code = str(random.randint(1000, 9999))
    sender = EMAIL_HOST_USER
    recipient_list = [email]
    if send_mail(subject, code, sender, recipient_list):
        new_code = VerificationCodeModel.objects.create(code=code, email=email)
        new_code.save()
        return True
    return False


def verify_code_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        code = VerificationCodeModel.objects.filter(code=code).first()
        tashkent_timezone = pytz.timezone('Asia/Tashkent')
        current_datatime_tashkent = datetime.now(tashkent_timezone)
        if current_datatime_tashkent - timedelta(minutes=2) <= code.send_time:
            UsersModel.objects.update(is_active=True)
            VerificationCodeModel.objects.filter(code=code).delete()
            return redirect('users:home')
        else:
            text = "Your code is invalid"
            return HttpResponse(text)


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_activate = True
            send_activation_email(form.cleaned_data['email'])

            form.save()
            return render(request, 'verify-code.html')
        else:
            text = form.errors
            return HttpResponse(text)
    else:
        return render(request, 'index.html')


def smm_view(request, pk):
    users = UsersModel.objects.all()
    if pk == 3:
        users = UsersModel.objects.filter(job__title__icontains='smm')

    context = {
        'users': users
    }
    return render(request, 'smm.html', context=context)


def graph_designer(request, pk):
    users = UsersModel.objects.all()
    if pk == 4:
        users = UsersModel.objects.filter(job__title__icontains='graphic_designer')
        context = {
            'users': users
        }
        return render(request, 'graphic-designer.html', context=context)


def crm_view(request, pk):
    users = UsersModel.objects.all()
    if pk == 5:
        users = UsersModel.objects.filter(job__title__icontains='crm')
        context = {
            'users': users
        }
        return render(request, 'crm.html', context=context)
