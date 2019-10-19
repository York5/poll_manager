from datetime import timedelta, datetime
from urllib.parse import urlencode
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404

from webapp.forms import PollForm, ChoiceForm
from django.urls import reverse, reverse_lazy
from webapp.models import Choice, Poll
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ChoiceInPollCreateView(CreateView):
    model = Choice
    form_class = ChoiceForm

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get('pk'))
        choice = poll.choices.create(**form.cleaned_data)
        return redirect('poll_view', pk=choice.poll.pk)


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'choice/update.html'
    form_class = ChoiceForm
    context_object_name = 'choice'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = 'choice/delete.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.poll.pk})
