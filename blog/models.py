from django.db import models
from tinymce.models import HTMLField
from taggit.managers import TaggableManager


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    link = models.SlugField('Ссылка на детальную страницу', max_length=50, unique=True,
                            help_text='Если автоматически сгенерированная ссылка вам не подходить, то измените ее '
                                      'вручную')
    anons = models.CharField('Анонс', max_length=250, blank=True, null=True,
                             help_text='Если оставить пустой, то анонс создаться из первого абзаца новости!')
    full_text = HTMLField('Статья')
    date = models.DateTimeField('Дата публикации')
    tags = TaggableManager('Теги', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блог'
