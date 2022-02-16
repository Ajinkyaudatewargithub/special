from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('exercise/', views.ExerciseView.as_view(), name='exercise'),
    path('question/<int:id>', views.BriefQuestionView, name='question'),
    path('articles/', views.Articles, name='article'),
    path('blog/<int:id>', views.FullBlog, name='blog'),
]