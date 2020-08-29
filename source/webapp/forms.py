from django import forms
from .models import Poll,Choice





class PollForm(forms.ModelForm):
    question = forms.CharField(max_length=300, required=True, label='Описание')

    class Meta:
        model = Poll
        fields = ['question']



class ChoceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']