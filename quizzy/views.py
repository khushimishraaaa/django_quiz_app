import json
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
import random

# Create your views here.


def index(request):
    context = {'categories': Category.objects.all()}

    if request.GET.get('category'):
        return redirect("/quizz/?category={}".format(request.GET.get('category')))
    
    return render(request, 'quizzy/home.html', context)

def login(request):

    form = Loginform(request, data=request.POST)

    if form.is_valid():
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            auth.login(request, user)

            return redirect("")
    
    context = {'loginForm': form}  
    
    return render(request, 'quizzy/login.html', context=context)

def register(request):
    
    form = CreateUserForm()
    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('my-login')

    context = {'registerForm': form}    
    
    return render(request, 'quizzy/register.html', context=context)

def user_logout(request):

    auth.logout(request)

    return redirect('my-login')


@login_required(login_url='my-login')
def quiz(request):
    context = {'category': request.GET.get('category')}
    return render(request, 'quizzy/quiz.html', context)


def get_quizz(request):
    question_objs = Question.objects.all()
    if request.GET.get('category'):
        question_objs = question_objs.filter(categories__category_name__icontains=request.GET.get('category'))

    question_objs = list(question_objs)
    data = []
    random.shuffle(question_objs)
    for question_obj in question_objs:
        data.append({
            "uid": question_obj.uid,
            "categories": question_obj.categories.category_name,
            "question_text": question_obj.question_text,
            "marks": question_obj.marks,
            "answers": question_obj.get_answer()
        })

    payload = {'status': 200, 'data': data}

    return JsonResponse(payload)

@csrf_exempt
def submit_quiz(request):
    if request.method == 'POST':
        category = request.POST.get('category')  
        total_marks = int(request.POST.get('totalMarks', 0))  

       
        return JsonResponse({'status': 'success', 'message': 'Quiz submitted successfully', 'totalMarks': total_marks})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    

