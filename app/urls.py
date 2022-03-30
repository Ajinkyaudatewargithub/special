from django.urls import path
from . import views 
from app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('exercise/', views.ExerciseView, name='exercise'),
    path('question/<slug:slug_text>', views.BriefQuestionView, name='question'),
    path('articles/', views.Articles, name='article'),
    path('blog/<slug:slug_text>/', views.FullBlog, name='blog'),
]