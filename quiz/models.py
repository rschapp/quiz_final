from django.db import models

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
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_text = models.CharField(max_length = 200)

    def __str__(self):
        return self.question_text

#model for correct answers
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length = 200)
    is_correct = models.BooleanField(default= False)

    def __str__(self):
        return self.answer_text

#model for user taking quiz
class QuizTaker(models.Model):
    user = models.CharField(max_length = 20)
    score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.user.username


#model for inputed answer
class UserAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)




