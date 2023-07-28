from django.urls import path
from .views import courses_list, course_detail, category_detail,tag_detail, search

urlpatterns = [
    path('', courses_list, name='courses_list'),
    path('<slug:category_slug>/<int:course_id>/', course_detail, name='course_detail'),
    path('categories/<slug:category_slug>/', category_detail, name='category_detail'),
    path('tags/<slug:tag_slug>/', tag_detail, name='tag_detail'),
    path('search/', search, name='search')
]
