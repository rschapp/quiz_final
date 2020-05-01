from django.shortcuts import render
from django.http import HttpResponse
from .models import Quiz, Question, Answer, Guess, TakenQuiz, Taker
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.db.models import Count, Sum
from django.views.generic import CreateView, ListView, UpdateView
from django.views import View
from django.views import generic
from django.template import RequestContext
from .forms import QuestionForm, BaseAnswerInlineFormSet, TakeQuizForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

def index(request):
    num_quizzes = Quiz.objects.all().count()
    context = {
    'num_quizzes': num_quizzes,
}
    
    return render(request, 'index.html', context=context)


class QuizListView(generic.ListView):
    model = Quiz

class QuizDetailView(generic.DetailView):
    model = Quiz

class QuizResultsView(View):
    template_name = 'templates/quiz_result.html'
    def get(self, request, *args, **kwargs):
        quiz = Quiz.objects.get(id = kwargs['pk'])
        questions = Question.objects.filter(quiz =quiz)
        #questions = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'questions':questions,
                      'quiz':quiz})

class TakenQuizView(View):
    model = TakenQuiz
    context_object_name = 'taken_quizzes'

def take_quiz(request, pk):
    quiz = get_object_or_404(Quiz, pk=pk)
    taker = Taker
    total_questions = 10
    unanswered_questions = taker.get_unanswered_questions(quiz)
    question = unanswered_questions.first()
    
    if request.method == 'POST':
            form = TakeQuizForm(question=question, data=request.POST)
            if form.is_valid():
                with transaction.atomic():
                    taker_answer = form.save(commit=False)
                    taker_answer.taker = taker
                    taker_answer.save()
                    if student.get_unanswered_questions(quiz).exists():
                        return redirect('take_quiz', pk)
                    else:
                        correct_answers = taker.quiz_answers.filter(answer__question__quiz=quiz, answer__is_correct=True).count()
                        percentage = round((correct_answers / total_questions) * 100.0, 2)
                        TakenQuiz.objects.create(taker=taker, quiz=quiz, score=correct_answers, percentage= percentage)
                        taker.score = TakenQuiz.objects.filter(taker=taker).aggregate(Sum('score'))['score__sum']
                        taker.save()
                        return redirect('quiz_results', pk)
    else:
        form = TakeQuizForm()
        return render(request, 'quiz/take_quiz_form.html', {
                      'quiz': quiz,
                      'question': question,
                      'form': form,
                      'total_questions': total_questions
                      })

