from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy

from webapp.forms import AnswerForm
from webapp.models import Answer, Poll, Choice
from django.views.generic import ListView, DetailView, CreateView, UpdateView


class AnswerCreateView(CreateView):
    model = Answer
    template_name = 'answer/answer.html'
    form_class = AnswerForm

    def dispatch(self, request, *args, **kwargs):
        self.poll = self.get_poll()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.poll.choices.create(**form.cleaned_data)
        return redirect('poll_view', pk=self.poll.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'].fields['choice'].queryset = Choice.objects.filter(poll=self.get_poll())
        context['poll'] = self.get_poll()
        return context

    def get_poll(self):
        poll_pk = self.kwargs.get('pk')
        return get_object_or_404(Poll, pk=poll_pk)
