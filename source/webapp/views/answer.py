
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from webapp.models import Poll,Answer,Choice
from webapp.forms import PollForm, SimpleSearchForm


class AnswerView(View):
    def get(self, request, *args, **kwargs):
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        choices = poll.choices.all()
        context = {
            'poll': poll,
            'choices': choices
        }
        return render(request, 'answer/index_answer.html', context)

    def post(self,request, *args, kwargs):
        pk = request.POST['answers']
        answers = get_object_or_404(Choice, pk=pk)
        poll = get_object_or_404(Poll, pk=kwargs['pk'])
        Answer.objects.create(answers=answers, poll=poll)
        return redirect('index')
