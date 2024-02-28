from django.contrib import admin
from jobs.models import JobModel





@admin.register(JobModel)
class JobModelAdmin(admin.ModelAdmin):
    list_display = ['title']
