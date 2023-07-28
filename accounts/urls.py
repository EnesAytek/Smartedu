from django.urls import path
from .views import user_login, user_register, user_dashboard, user_logout,enroll_the_course,release_the_course

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name='user_register'),
    path('dashboard/', user_dashboard, name='user_dashboard'),
    path('logout/', user_logout, name='user_logout'),
    path('enroll_the_course/', enroll_the_course, name='enroll_the_course'),
    path('release_the_course/', release_the_course, name='release_the_course'),
]
