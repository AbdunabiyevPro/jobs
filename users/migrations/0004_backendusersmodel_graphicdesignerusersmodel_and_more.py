# Generated by Django 5.0.2 on 2024-02-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_frontendusersmodel_delete_usersmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackendUsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('telegram_link', models.URLField()),
                ('part_link', models.URLField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='GraphicDesignerUsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('telegram_link', models.URLField()),
                ('part_link', models.URLField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='MobilografUsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('telegram_link', models.URLField()),
                ('part_link', models.URLField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='SmmUsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('telegram_link', models.URLField()),
                ('part_link', models.URLField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='TelegramUsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('description', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('telegram_link', models.URLField()),
                ('part_link', models.URLField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.DeleteModel(
            name='VerificationCodeModel',
        ),
    ]
