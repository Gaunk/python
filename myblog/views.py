from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Post, Author
import pytz
from datetime import datetime
import datetime
# Create your views here.


def home(request):
    posts = Post.objects.all()
    now = datetime.datetime.now()
    context = {'posts': posts,
               'now': now,
               'otherdate': now + datetime.timedelta(days=0),
               }
    return render(request, 'base_code.html', context)


def blog(request):
    week_ago = datetime.date.today() - datetime.timedelta(days=8)
    trends = Post.objects.filter(
        publish=True, time_upload__gte=week_ago).order_by('-read')
    now = datetime.datetime.now()
    context = {
        'posts': Post.objects.filter(publish=True),
        'trends': trends[:5],
        'now': now,
        'otherdate': now + datetime.timedelta(days=0),

    }
    return render(request, 'blog.html', context)


def postingan(request, url):
    post = Post.objects.filter(publish=True)
    context = {
        'post': post,
    }
    return render(request, 'postingan.html', context)
