from django.db import models

# Модель формы контакты
class Feedbacks(models.Model):
    name = models.CharField('Имя', max_length=50)
    email = models.CharField('Почта', max_length=50)
    text = models.TextField('Текст')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

