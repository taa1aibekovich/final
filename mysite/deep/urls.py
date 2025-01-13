from .views import *
from django.urls import path, include
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'faculty', FacultyViewSet, basename='faculty')
router.register(r'professor', ProfessorViewSet, basename='professor')
router.register(r'student', StudentViewSet, basename='student')
router.register(r'curse', CourseViewSet, basename='curse')
router.register(r'office', OfficeViewSet, basename='office')
router.register(r'schedule', ScheduleViewSet, basename='schedule')
router.register(r'record', RecordViewSet, basename='record')
router.register(r'homework', HomeworkViewSet, basename='homework')
router.register(r'delivery', DeliveryViewSet, basename='delivery')

urlpatterns = [
    path('', include(router.urls)),
]
