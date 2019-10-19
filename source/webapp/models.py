from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=300, null=False, blank=False, verbose_name='Question')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.question


class Choice(models.Model):
    text = models.TextField(max_length=300, null=False, blank=False, verbose_name='Text')
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE, verbose_name='Poll', related_name='choices')

    def __str__(self):
        return self.text