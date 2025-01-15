from django.urls import path,include
from app import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('education/',views.eduction,name='education'),
    path('projects/',views.project,name='projects'),
    path('resume/',views.resume,name='resume'),
    path('contact/',views.contact,name='contact'),
]
