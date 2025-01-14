from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['last_name', 'first_name']


class FacultySerializers(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['faculty_name', 'description']


class ProfessorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = ['user', 'department', 'title', 'professor_description']


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['user', 'department', 'enrollment_date', 'graduation_date']


class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name', 'code', 'description', 'department', 'professor']


class OfficeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['room_number', 'building', 'capacity']



class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['course', 'classroom', 'start_time', 'end_time', 'day_of_week']



class RecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['student', 'course', 'date_enrolled', 'grade']



class HomeworkSerializers(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ['course', 'title', 'description', 'due_date']


class DeliverySerializers(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ['homework', 'student', 'submission_date', 'grade', 'feedback']
