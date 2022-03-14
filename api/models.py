#from pyexpat import model
from statistics import mode
from tkinter import CASCADE
import django
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE, related_name='user', null=True)
    comments = models.ForeignKey('Comments', related_name='comments',
                                 on_delete=models.CASCADE, blank=True, null=True)


class Comments(models.Model):
    ''' reply_to_comment идентификатор комментария, в ответ на который должен быть добавлен новый
    комментарийидентификатор комментария, в ответ на который должен быть добавлен новый комментарий'''

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE, related_name='article', null=True)
    body = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='Comments', null=True)  #post_id
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name='Comments'
    )



