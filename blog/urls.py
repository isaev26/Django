from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<str:link>.html', views.BlogsDetailView.as_view(), name='blog_detail'),
]
