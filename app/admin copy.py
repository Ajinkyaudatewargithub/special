from django.contrib import admin
from . models import Language, ExerciseQuestions, Questions, Blog

# Register your models here.

@admin.register(Language)
class AdminLanguages(admin.ModelAdmin):
    list_display = ['name', 'description']

@admin.register(ExerciseQuestions)
class AdminExerciseQuestions(admin.ModelAdmin):
    list_display = ['head', 'topic_tag']

@admin.register(Questions)
class AdminQuestions(admin.ModelAdmin):
    list_display = ['heading']
    class Media:
        js= ('tinyInject.js',)

@admin.register(Blog)
class AdminBlog(admin.ModelAdmin):
    list_display = ['title','date_publish']
    class Media:
        js= ('tinyInject.js',)