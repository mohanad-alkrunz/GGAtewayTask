from django.contrib import admin
from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models
# Register your models here.

@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
   
    list_display = ['first_name', 'father_name',
                    'last_name', 'date_of_birth']
    

 