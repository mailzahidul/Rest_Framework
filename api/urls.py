from django.urls import path
from .views import student_info, student_info_list
from . import views
urlpatterns = [
    path('student_info/<int:id>', views.student_info, name='student_info'),
    path('student_info_list', views.student_info_list, name='student_info_list'),
    path('student_create', views.student_create, name='student_create')
]
