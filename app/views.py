from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from .models import Language, Questions, ExerciseQuestions, Blog
from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm
# Create your views here.

class Login(LoginView):
    template_name='app/login.html' 
    authentication_form=LoginForm

class Logout(LogoutView):
    template_name='app/logout.html'


class DashBoard(TemplateView):
    template_name = 'app/dashboard.html'
    model = Questions, ExerciseQuestions, Blog
    



class HomeView(View):
    def get(self, request):
        lang = Language.objects.all()
        bg = Blog.objects.all()
        context = {'language':lang, 'blogs':bg}
        return render(request, 'app/home.html', context)

class ExerciseView(View):
    def get(self, request):
        question = ExerciseQuestions.objects.all()
        context = {'questions':question}
        return render(request, 'app/exercise.html', context)

def BriefQuestionView(request, id):
    q = Questions.objects.get(id=id)
    context = {'question':q}
    return render(request, 'app/briefq.html', context)


def Articles(request):
    blog = Blog.objects.all()
    context = {'blogs':blog}
    return render(request, 'app/article.html', context)

def FullBlog(request, id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}
    return render(request, 'app/fullblog.html', context)