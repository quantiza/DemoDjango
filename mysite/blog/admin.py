# -*- coding: utf-8 -*-

from django.contrib import admin
from blog import models

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time')


admin.site.register(models.BlogPost, BlogPostAdmin)
admin.site.register(models.Article, ArticleAdmin)