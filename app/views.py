from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.base import TemplateView
from .models import Questions, Topic, Blog
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
    model = Questions, Blog
    
    
class HomeView(View):
    def get(self, request):
        bg = Blog.objects.all()
        context = {'blogs':bg}
        return render(request, 'app/home.html', context)

def ExerciseView(request):

    if request.method=='POST':
        id = request.POST['FilterSelect']
        question = Questions.objects.filter(topic_tag=id)
        tp = Topic.objects.all()
        context = {'questions':question, 'topics':tp}
        return render(request, 'app/exercise.html', context)

    else:
        question = Questions.objects.all()
        tp = Topic.objects.all()
        context = {'questions':question, 'topics':tp}
        return render(request, 'app/exercise.html', context)

def BriefQuestionView(request, slug_text):
    q = Questions.objects.filter(slug=slug_text)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse("<h1>Page Not Found!</h1>")
    context = {'question':q}
    return render(request, 'app/briefq.html', context)


def Articles(request):
    blog = Blog.objects.all()
    context = {'blogs':blog}
    return render(request, 'app/article.html', context)

def FullBlog(request, slug_text):
    blog = Blog.objects.filter(slug=slug_text)
    if blog.exists():
        blog = blog.first()
    else:
        return HttpResponse("<h1>Page Not Found!</h1>")

    context = {'blog':blog}
    return render(request, 'app/fullblog.html', context)