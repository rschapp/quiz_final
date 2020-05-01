from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Quiz(models.Model):
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=280)

    class Meta:
        verbose_name_plural = "Quizzes"

    def __str__(self):
        return self.name

#model for quesitons
class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE,related_name='questions')
    text = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.text
#model for correct answers
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='answers')
    text = models.CharField(max_length = 200)
    is_correct = models.BooleanField('Correct answer', default=False)
    
    def __str__(self):
        return self.text

#model for user taking quiz
class Taker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    score = models.IntegerField(default=0)
    
    def get_unanswered_questions(quiz):
        answered_questions = Question.objects.filter(quiz =quiz).filter(answers__question__quiz=quiz).values_list('answers__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions
    
    def __str__(self):
        return self.user.username
class TakenQuiz(models.Model):
    user = models.ForeignKey(Taker, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.IntegerField()
    percentage = models.FloatField()

#model for inputed answer
class Guess(models.Model):
    taker = models.ForeignKey(Taker, on_delete = models.CASCADE,related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE,related_name='+')




