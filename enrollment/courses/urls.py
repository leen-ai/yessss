from django.urls import path
from . import  views

urlpatterns = [
    path('courses/', views.courses, name='courses'),
    path('courses/schedule',views.schedule, name='schedule'),
    path('courses/sub',views.sub, name='sub')
]