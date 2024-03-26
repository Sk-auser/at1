from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, QuizResult

@login_required
def quiz_home(request):
    # Logic to display the home page of the quiz app
    return render(request, 'quiz/quiz_home.html')

@login_required
def take_quiz(request):
    # Logic to retrieve questions and display the quiz form
    questions = Question.objects.all()
    return render(request, 'quiz/take_quiz.html', {'questions': questions})

@login_required
def submit_answer(request):
    # Logic to process submitted answers
    if request.method == 'POST':
        user = request.user
        question_id = request.POST['question_id']
        user_answer = request.POST['user_answer']
        question = Question.objects.get(pk=question_id)
        is_correct = (user_answer == question.answer_text)
        QuizResult.objects.create(user=user, question=question, user_answer=user_answer, is_correct=is_correct)
    return redirect('quiz:quiz_results')

@login_required
def quiz_results(request):
    # Logic to display quiz results for the current user
    quiz_results = QuizResult.objects.filter(user=request.user)
    return render(request, 'quiz/quiz_results.html', {'quiz_results': quiz_results})