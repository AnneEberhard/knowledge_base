from django.contrib import admin

from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'created_at', 'author', 'text')
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title',)


admin.site.register(Article, ArticleAdmin)
