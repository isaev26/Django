from django.forms import ModelForm, Textarea, TextInput, forms
from .models import Feedbacks
from _datetime import datetime, timedelta
from captcha.fields import CaptchaField


class FeedbacksForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Feedbacks
        fields = ['name', 'email', 'text', 'date']

        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name@example.com',
            }),
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш текст',
                'rows': '5'
            }),
            'date': TextInput(attrs={
                'class': 'form-control',
                'placeholder': datetime.now() + timedelta(hours=3),  # добавляю 3 часа на серверной время
                'value': datetime.now() + timedelta(hours=3),
            }),
        }
