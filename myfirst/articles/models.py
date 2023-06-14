from django.db import models


class Article(models.Model):
    title = models.CharField('название статьи', max_length=200)
    text = models.TextField('текст статьи')
    pub_date = models.DateTimeField('дата публикации')


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField('имя автора', max_length=50)
    comment = models.CharField('текст ккомментария', max_length=50)
