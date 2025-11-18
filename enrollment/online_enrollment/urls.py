from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path
from online_enrollment import views

urlpatterns = [
    # Student
    path('students/', views.student_list, name='student_list'),
    path('students/add/', views.add_edit_student, name='add_student'),
    path('students/edit/<int:pk>/', views.add_edit_student, name='edit_student'),

    # Courses
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_edit_course, name='add_course'),
    path('courses/edit/<int:pk>/', views.add_edit_course, name='edit_course'),

    # Schedule
    path('schedule/', views.course_list, name='course_list'),
    path('schedule/add/', views.add_edit_view, name='add_schedule'),
    path('schedule/edit/<int:pk>/', views.add_edit_course, name='edit_schedule'),
    path('schedule/', views.course_list, name='course_list'),


    # Enrollment
    path('enrollment/', views.enrollment_list, name='enrollment_list'),
    path('enrollment/add/', views.enrollment_list, name='add_enrollment'),
    path('enrollment/edit/<int:pk>/', views.enrollment_list, name='edit_enrollment'),

    # Student Background
    path('background/', views.student_background_list, name='student_background_list'),
    path('background/add/', views.add_edit_student_background, name='add_student_background'),
    path('background/edit/<int:pk>/', views.add_edit_student_background, name='edit_student_background'),

    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home_view, name='home'),       # Corrected
    path('logout/', views.logout_view, name='logout'), # Add a proper logout URL
]
