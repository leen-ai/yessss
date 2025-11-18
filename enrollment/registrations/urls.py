from django.urls import path
from . import  views

urlpatterns = [
    path('registrations/', views.registrations, name='registrations'),
    path('registrations/birthdate', views.birthdate, name='birthdate'),
    path('registrations/school', views.school, name='school')
]