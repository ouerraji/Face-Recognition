from django.urls import path
from . import views

app_name = 'face_recognition'

urlpatterns = [
    path('', views.index, name='index'),
path('capture_student/', views.student_registration, name='student_registration'),
]