from django.urls import path
from . import views


urlpatterns = [
               path('',views.index,name='index'),
               path('quizzes/', views.QuizListView.as_view(), name='quizzes'),
               path('quizzes/<int:pk>', views.QuizDetailView.as_view(), name='quiz-detail'),
               path('quizzes/<int:pk>/take_quiz', views.take_quiz, name='take_quiz'),
               path('quizzes/<int:pk>/results/', views.QuizResultsView.as_view(), name='quiz_results')
               ]
