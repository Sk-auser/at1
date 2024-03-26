from django.db import models
from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    answer_text = models.CharField(max_length=100)

def __str__(self):
    return "{} - {}".format(self.country.name, self.question_text)

class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_answer = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    
def __str__(self):
    return "{} - {}".format(self.country.name, self.question_text)
