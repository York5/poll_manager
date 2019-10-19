from datetime import timedelta, datetime
from urllib.parse import urlencode

from django.db.models import Q
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
    model = Article

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article = self.object
        tags = article.tags.all()
        context['form'] = ArticleCommentForm()
        context['tags'] = tags
        comments = article.comments.order_by('-created_at')
        self.paginate_comments_to_context(comments, context)
        return context

    def paginate_comments_to_context(self, comments, context):
        paginator = Paginator(comments, 3, 0)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        context['paginator'] = paginator
        context['page_obj'] = page
        context['comments'] = page.object_list
        context['is_paginated'] = page.has_other_pages()