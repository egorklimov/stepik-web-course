# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
    '''
        QuestionManager - менеджер модели Question
        new - метод возвращающий последние добавленные вопросы
        popular - метод возвращающий вопросы отсортированные по рейтингу
    '''
    def get_queryset(self):
        return super().get_queryset()

    def new(self):
        return super().get_queryset().order_by('-added_at')[:5]

    def popular(self):
        return super().get_queryset()


class Question(models.Model):
    '''
        Question - вопрос
        title - заголовок вопроса
        text - полный текст вопроса
        added_at - дата добавления вопроса
        rating - рейтинг вопроса (число)
        author - автор вопроса
        likes - список пользователей, поставивших "лайк"
    '''
    objects = QuestionManager()
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.OneToOneField(User)
    likes = models.ManyToManyField(User, related_name="likes_set")

    def __str__(self):
        return "%s %s" % (self.author, self.title)

    class Meta:
        ordering = ('rating', 'added_at')


class Answer(models.Model):
    '''
        Answer - ответ
        text - текст ответа
        added_at - дата добавления ответа
        question - вопрос, к которому относится ответ
        author - автор ответа
    '''
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.OneToOneField(Question)
    author = models.OneToOneField(User)

    def __str__(self):
        return "%s %s" % (self.question.id. self.author.email)
