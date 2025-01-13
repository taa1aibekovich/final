from django_filters.rest_framework import FilterSet
from .models import Faculty, Course


class FacultyFilter(FilterSet):
    class Meta:
        model = Faculty
        fields = {
            'department': ['exact']
        }


class CursFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'course_name': ['exact']
        }

