from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api/get-quizz/', views.get_quizz),
    path('quizz/', views.quiz),
    path('api/submit-quiz/', views.submit_quiz, name='submit_quiz'),
    
]