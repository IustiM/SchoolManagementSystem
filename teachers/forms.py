from django import forms

from .models import *


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('name', 'email', 'phone', 'address')


# QuestionFormSet = inlineformset_factory(
#     Exam,
#     Question,
#     fields=['title'],
#     formset=BaseQuestionFormSet,
#     extra=1,
#     can_delete=True,
# )


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'start_time', 'end_time']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'start_time': forms.TimeField(),
            'end_time': forms.TimeField()

        }


class BaseQuestionFormSet(forms.BaseInlineFormSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.queryset = Question.objects.none()

    def clean(self):
        super().clean()
        for form in self.forms:
            if not form.cleaned_data.get('DELETE', False):
                if not form.cleaned_data.get('title'):
                    raise forms.ValidationError('All questions must have a title.')

    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields[f'answer_{index}'] = forms.ModelChoiceField(
            queryset=Answer.objects.none(),
            widget=forms.RadioSelect(),
            required=False,
        )
