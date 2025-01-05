from django.contrib import admin
from .models import *
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Phone','Subject','Message']

admin.site.register(Contactus,ContactUsAdmin)