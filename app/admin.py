from django.contrib import admin
from . models import Questions, Blog, Topic

# Register your models here.

@admin.register(Topic)
class AdminTopic(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Questions)
class AdminQuestions(admin.ModelAdmin):
    list_display = ['title', 'topics', 'slug']
    class Media:
        js= ('tinyInject.js',)

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ['title','date_publish']
    class Media:
        js= ('tinyInject.js',)