from django import forms
from django.forms.utils import ValidationError
from django.db import transaction
from .models import Quiz, Question, Answer, Guess, TakenQuiz, Taker

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('text',)

class BaseAnswerInlineFormSet(forms.BaseInlineFormSet):
    def clean(self):
        super().clean()
        has_one_correct_answer = False
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if form.cleaned_data.get('is_correct', False):
                    has_one_correct_answer = True
                    break
            if not has_one_correct_answer:
                raise ValidationError('Mark at least one answer as correct.', code='no_correct_answer')

class TakeQuizForm(forms.ModelForm):
    answer = forms.ModelChoiceField(
                                    queryset=Answer.objects.none(),
                                    widget=forms.RadioSelect(),
                                    required=True,
                                    empty_label=None)
        
    class Meta:
        model = Guess
        fields = ('answer',)

        def __init__(self, *args, **kwargs):
            question = kwargs.pop('question')
            super().__init__(*args, **kwargs)
            self.fields['answer'].queryset = question.answers.order_by('text')

