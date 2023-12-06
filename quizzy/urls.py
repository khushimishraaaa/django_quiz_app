from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=""),
    path('register/', views.register,name='register'),
    path('login/', views.login, name='my-login'),
    path('user-logout/', views.user_logout, name='log-out'),
    path('api/get-quizz/', views.get_quizz),
    path('quizz/', views.quiz, name="quiz"),
    path('api/submit-quiz/', views.submit_quiz, name='submit_quiz'),
    
]