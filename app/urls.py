from django.urls import path
from . import views 
from app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('exercise/', views.ExerciseView.as_view(), name='exercise'),
    path('question/<int:id>', views.BriefQuestionView, name='question'),
    path('articles/', views.Articles, name='article'),
    path('blog/<int:id>', views.FullBlog, name='blog'),
]