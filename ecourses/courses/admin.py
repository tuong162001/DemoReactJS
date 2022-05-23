from .models import Course, Category, Lesson, Comment, User
from django.contrib import admin

# Register your models here.
admin.site.register(Course)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Comment)
admin.site.register(User)