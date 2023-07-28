from django.contrib import admin
from .models import Course, Category, Tag


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'avaliable',
    )
    list_filter = ('avaliable',)
    search_fields = ('name', 'description')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'slug',
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'slug',
    )