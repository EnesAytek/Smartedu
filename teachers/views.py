from django.shortcuts import render
from .models import Teacher
from courses.models import Course

def teacher_list(request):
    teachers = Teacher.objects.all()
    context = dict (
        teachers=teachers,
    )
    return render(request, 'teachers.html', context)

def teacher_detail(request, teacher_id):
    teachers = Teacher.objects.filter(id=teacher_id)
    courses = Course.objects.filter(teacher__id=teacher_id)
    context = dict(
        teachers=teachers,
        courses=courses,
    )
    return render(request, 'teacher_detail.html', context)