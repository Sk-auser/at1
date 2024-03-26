from django.contrib import admin
from .models import Country, Question, QuizResult

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'capital')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('country', 'question_text', 'answer_text')

@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'user_answer', 'is_correct')
