from django.contrib import admin
from .models import *
# Register your models here.

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['Name','Email','Phone','Subject','Message']

class EducationAdmin(admin.ModelAdmin):
    list_display = ['title','school_name','university_name','location','duration']

class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','company','skills','location','duration']

class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['title','back']

admin.site.register(Contactus,ContactUsAdmin)
admin.site.register(Eduction,EducationAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Projects,ProjectsAdmin)
admin.site.register(image)
admin.site.register(Filefield)