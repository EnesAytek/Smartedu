from django.urls import path
from .views import teacher_list, teacher_detail

urlpatterns = [
    path('', teacher_list, name='teacher_list'),
    path('teacher/<int:teacher_id>/', teacher_detail, name='teacher_detail')
]
