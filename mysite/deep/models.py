from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    phone_number = PhoneNumberField()

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'


class Faculty(models.Model):
    faculty_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f'{self.faculty_name}'


class Professor(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='department_user')
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='department')
    title = models.CharField(max_length=32)
    professor_description = models.TextField()

    def __str__(self):
        return f'{self.department} - {self.title}'


class Student(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='student_department')
    enrollment_date = models.DateField(auto_now_add=True)
    graduation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.department}'


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    description = models.TextField()
    department = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='course_department')
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='professors')

    def __str__(self):
        return f'{self.course_name}'


class Office(models.Model):
    room_number = models.CharField(max_length=10)
    building = models.CharField(max_length=100)
    capacity = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.room_number}'


class Schedule(models.Model):
    course = models.ManyToManyField(Course, related_name='curse')
    classroom = models.ManyToManyField(Office, related_name='classroom')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    STATUS_CHOICES = (
        ('Понедельник', 'Понедельник'),
        ('Вторник', 'Вторник'),
        ('Среда', 'Среда'),
        ('Четверг', 'Четверг'),
        ('Пятница', 'Пятница'),
    )
    day_of_week = models.CharField(choices=STATUS_CHOICES, max_length=20)

    def __str__(self):
        return f'{self.course}- {self.classroom}'


class Record(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='home_work')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='cours_work')
    date_enrolled = models.DateField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.course}"


class Homework(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()

    def __str__(self):
        return f"{self.title} for {self.course}"


class Delivery(models.Model):
    homework = models.ForeignKey(Homework, on_delete=models.CASCADE, related_name='delivery_homework')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_delivery')
    submission_date = models.DateField(auto_now_add=True)
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.student}- {self.homework}'
