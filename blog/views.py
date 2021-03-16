from django.shortcuts import render
from .models import Articles
from django.views.generic import DetailView

# Вывод список постов из 6 элемента
def blog_index(request):
    blog = Articles.objects.order_by('-date')[:6]
    data = {
        'title': 'Блог',
        'blog': blog
    }
    return render(request, 'blog/blog_index.html', data)

# Детальный просмотр поста
class BlogsDetailView(DetailView):
    model = Articles
    template_name = 'blog/blog_detail.html'
    context_object_name = 'article'
    slug_field = 'link'
    slug_url_kwarg = 'link'
