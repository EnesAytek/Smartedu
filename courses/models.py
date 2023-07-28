from django.db import models
from autoslug import AutoSlugField
from teachers.models import Teacher
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = AutoSlugField(populate_from='name')



    def __str__(self):
        return self.name
    

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = AutoSlugField(populate_from='name')



    def __str__(self):
        return self.name


class Course(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    students = models.ManyToManyField(User, blank=True, related_name='courses_joined')
    description = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default_course_image.jpg")
    date = models.DateTimeField(auto_now=True)
    avaliable = models.BooleanField(default=True)
   


    def __str__(self):
        return self.name
    

