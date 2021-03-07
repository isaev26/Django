from django.shortcuts import render
from .forms import FeedbacksForm
import random

def index(request):
    lines = open('../myapp/main/static/sitat.txt').read().splitlines()
    line = random.choice(lines)
    data = {
        'title': 'Главная страница',
        'line': line,
    }
    return render(request, 'main/index.html', data)


def about(request):
    data = {
        'title': 'Обо мне'
    }
    return render(request, 'main/about.html', data)


def contact(request):
    error = ''
    if request.method == 'POST':
        form = FeedbacksForm(request.POST)
        if form.is_valid():
            form.save()
            error = 'Форма отправлен!'
        else:
            error = 'Форма не верно заполнен!!'

    form = FeedbacksForm()
    data = {
        'title': 'Контакты',
        'form': form,
        'error': error
    }
    return render(request, 'main/contact.html', data)
