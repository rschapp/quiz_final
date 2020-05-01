from django.contrib import admin
import nested_admin
from .models import Quiz, Question, Answer, Guess, TakenQuiz, User

# Register your models here.

class AnswerInline(nested_admin.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4

class QuestionInline(nested_admin.NestedTabularInline):
    model = Question
    inlines = [AnswerInline,]
    extra = 3

class QuizAdmin(nested_admin.NestedModelAdmin):
    inlines = [QuestionInline,]

# Register your models here.
admin.site.register(Quiz,QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Guess)
admin.site.register(TakenQuiz)

