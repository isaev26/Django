from django.contrib import admin
from .models import Articles

# Генерация ЧПУ (slug) из title поста
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'link': ('title',)}


admin.site.register(Articles, BlogAdmin)
