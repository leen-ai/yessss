from django.db import models

class TestingDatabase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    registrations_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"

class Student(models.Model):
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=11)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    LRN = models.CharField(max_length=12)
    
    def __str__(self):
        return f"{self.name}"    


class Course(models.Model):
    subject = models.CharField(max_length=100)
    course_code = models.CharField(max_length=11)
    section = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.subject}"
    
class Schedule(models.Model):
    course_id = models.CharField(max_length=100)
    schedule_id = models.CharField(max_length=100)
    instructor_id = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    day = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.course_id}"

class Enrollment(models.Model):
    enrollment_id = models.CharField(max_length=100)
    student_id = models.CharField(max_length=9)
    course_id = models.CharField(max_length=100)
    enrollment_date = models.CharField(max_length=100)
    payment = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.enrollment_id}"

class StudentBackground(models.Model):
    mother_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    guardian_contact_no = models.CharField(max_length=11)
    guardian_address = models.CharField(max_length=100)
    last_school_attended = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.mother_name}"
