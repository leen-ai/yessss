from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course, Schedule, Enrollment,StudentBackground

from .forms import (
    StudentForm, CourseForm, ScheduleForm,
    EnrollmentForm, StudentBackgroundForm
)

def add_edit_view(request, model, form_class, template_title, redirect_url, pk=None):
    instance = get_object_or_404(model, pk=pk) if pk else None
    if request.method == 'POST':
        form = form_class(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(redirect_url)
    else:
        form = form_class(instance=instance)
    return render(request, 'form_template.html', {'form': form, 'title': template_title})


def student_list(request):
    return render(request, 'studentprofile_list.html', {'students': Student.objects.all()})

def add_edit_student(request, pk=None):
    return add_edit_student(request, Student, StudentForm, 'Student', 'studentprofile', pk)


def course_list(request):
    return render(request, 'course_list.html', {'courses': Course.objects.all()})

def add_edit_course(request, pk=None):
    return add_edit_course(request, Course, CourseForm, 'Course', 'course_list', pk)


def schedule_list(request):
    return render(request, 'schedule_list.html', {'courses': Schedule.objects.all()})

def add_edit_schedule(request, pk=None):
    return add_edit_schedule(request, Schedule, ScheduleForm, 'Schedule', 'schedule_list', pk)


def enrollment_list(request):
    return render(request, 'enrollment_list.html', {'instructors': Enrollment.objects.all()})

def add_edit_enrollment(request, pk=None):
    return add_edit_enrollment(request, Enrollment, EnrollmentForm, 'Enrollment', 'enrollment_list', pk)


def student_background_list(request):
    return render(request, 'student_background_list.html', {'fees': StudentBackground.objects.all()})

def add_edit_student_background(request, pk=None):
    return add_edit_student_background(request, StudentBackground, StudentBackgroundForm, 'Student Background', 'student_background_list', pk)
