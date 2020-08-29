from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.urls import reverse,reverse_lazy
from django.views.generic import View, TemplateView,ListView,CreateView,UpdateView,DeleteView

from webapp.models import Poll
from webapp.forms import PollForm, SimpleSearchForm



class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'polls'
    paginate_by = 5
    paginate_orphans = 0

    def get_context_data(self, *, object_list=None, **kwargs):
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            kwargs['search'] = search
        kwargs['form'] = form
        return super().get_context_data(object_list=object_list, **kwargs)

    def get_queryset(self):
        data = Poll.objects.all()
        form = SimpleSearchForm(data=self.request.GET)
        if form.is_valid():
            search = form.cleaned_data['search']
            if search:
                data = data.filter(Q(question__icontains=search))

        return data.order_by('-created_at')

class PollView(TemplateView):
    template_name = 'poll/poll_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        pk = self.kwargs.get('pk')
        poll = get_object_or_404(Poll, pk=pk)

        context['poll'] = poll
        return context


class PollCreateView(CreateView):
    model = Poll
    form_class = PollForm
    template_name = 'poll/poll_create.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/poll_update.html'
    form_class = PollForm

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'poll/poll_delete.html'
    model = Poll
    success_url = reverse_lazy('index')