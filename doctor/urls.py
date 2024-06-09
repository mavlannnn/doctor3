from django.urls import path
from .views import *

urlpatterns = [
    path('user_profiles/', UserProfileViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='user_profile_list'),
    path('userprofile/<int:pk>/', UserProfileViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='user_profile_detail'),


    path('doctor/', DoctorViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='doctor_list'),
    path('doctors/<int:pk>/', DoctorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='doctor_detail'),


    path('medical_record/', MedicalRecordViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='medical_record_list'),
    path('medical_records/<int:pk>/', MedicalRecordViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='medical_record_detail'),


    path('appointment', AppointmentViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='appointment_list'),
    path('appointment/<int:pk>/', AppointmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='appointment_detail'),


    path('medication/', MedicationViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='medication_list'),
    path('medication/<int:pk>/', MedicationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='medication_detail'),


    path('fitness_program/', FitnessProgramViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='fitness_program_list'),
    path('fitness_program/<int:pk>/', FitnessProgramViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='fitness_program_detail'),


    path('notification/', NotificationViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='notification_list'),
    path('notification/<int:pk>/', NotificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}),
         name='notification_detail'),

]