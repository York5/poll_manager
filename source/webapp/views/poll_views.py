from datetime import timedelta, datetime
from urllib.parse import urlencode
from django.db.models import Q
from webapp.forms import PollForm, ChoiceForm
from django.urls import reverse, reverse_lazy
from webapp.models import Poll
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class PollIndexView(ListView):
    template_name = 'poll/index.html'
    context_object_name = 'polls'
    model = Poll
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 1


class PollView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = self.object
        context['form'] = ChoiceForm()
        choices = poll.choices.all()
        context['choices'] = choices
        return context


class PollCreateView(CreateView):
    form_class = PollForm
    model = Poll
    template_name = 'poll/create.html'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    model = Poll
    template_name = 'poll/update.html'
    form_class = PollForm
    context_object_name = 'poll'

    def get_success_url(self):
        return reverse('poll_view', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'poll/delete.html'
    context_object_name = 'poll'
    success_url = reverse_lazy('index')