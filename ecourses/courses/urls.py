from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from . import views

routers = routers.DefaultRouter()
routers.register("categories",views.CategoryViewSet,'category')
routers.register('courses',views.CourseViewSet,'course')
routers.register('lessons',views.LessonViewSet,'lesson')
routers.register('users',views.UserViewSet,'user')
routers.register('comments',views.CommentViewSet,'comment')

urlpatterns = [
    path('', include(routers.urls)),
    path('oauth2-info/',views.AuthInfo.as_view())
]