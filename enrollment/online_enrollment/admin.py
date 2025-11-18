from django.contrib import admin
from .models import TestingDatabase
from .models import Student
from .models import Course
from .models import Schedule
from .models import Enrollment
from .models import StudentBackground

admin.site.register(TestingDatabase)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Schedule)
admin.site.register(Enrollment)
admin.site.register(StudentBackground)