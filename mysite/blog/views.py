# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *
from datetime import datetime
from django.http import Http404
# Create your views here.


def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, index):
    try:
        post = Article.objects.get(id=index)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post})


def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})

