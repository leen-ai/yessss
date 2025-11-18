from django.urls import path
from . import  views

urlpatterns = [
    path('students/', views.students, name='students'),
    path('students/name', views.name, name='name'),
    path('students/id', views.id, name='id')
]