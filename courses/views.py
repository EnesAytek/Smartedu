from django.shortcuts import render
from .models import Course, Category, Tag
from teachers.models import Teacher
from django.contrib.auth.models import User


def courses_list(request):
    current_user = request.user
    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()
        courses = Course.objects.all().order_by('-date')
        for course in enrolled_courses:
            courses = courses.exclude(id=course.id)
    else:
        courses = Course.objects.all().order_by('-date')

    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = dict(
        courses=courses,
        categories=categories,
        tags=tags,
    )
    return render(request, 'courses.html', context)


def course_detail(request, category_slug, course_id):
    current_user = request.user
    course = Course.objects.get(category__slug=category_slug, id=course_id)
    if current_user.is_authenticated:
        enrolled_courses = current_user.courses_joined.all()
    else:
        enrolled_courses = course
    teachers = Teacher.objects.filter(course__id=course_id)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = dict(
        course = course,
        enrolled_courses=enrolled_courses,
        categories=categories,
        tags=tags,
        teachers=teachers,
    )
    return render(request, 'course.html', context)


def category_detail(request, category_slug):
    courses = Course.objects.all().filter(category__slug = category_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = dict(
        courses = courses,
        categories = categories,
        tags=tags,
    )
    return render(request, 'courses.html', context)

def tag_detail(request, tag_slug):
    courses = Course.objects.all().filter(tag__slug = tag_slug)
    categories = Category.objects.all()
    tags = Tag.objects.all()
    context = dict(
        courses = courses,
        categories = categories,
        tags=tags,
    )
    return render(request, 'courses.html', context)


def search(request):
    courses = Course.objects.filter(name__contains = request.GET['search'])  
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
        
    context = dict(
        courses = courses,
        categories = categories,
        tags=tags,
        )
    
    
    return render(request, 'courses.html', context)