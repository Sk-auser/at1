from django.urls import path
from . import views

app_name = 'quiz'

urlpatterns = [
    path('', views.quiz_home, name='quiz_home'),
    path('take_quiz/', views.take_quiz, name='take_quiz'),
    path('submit_answer/', views.submit_answer, name='submit_answer'),
    path('quiz_results/', views.quiz_results, name='quiz_results'),
    # Add more URL patterns as needed
]
