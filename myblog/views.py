from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from .models import Post, Author, ListHarga
import pytz
from datetime import datetime
import datetime
# Create your views here.


def home(request):
    biaya = Post.objects.all()

    # biaya = ListHarga.objects.all()
    now = datetime.datetime.now()
    context = {'biaya': ListHarga.objects.filter().first,
               'now': now,
               'otherdate': now + datetime.timedelta(days=0),
               }
    return render(request, 'base_code.html', context)


def blog(request):
    posts = Post.objects.all()
    now = datetime.datetime.utcnow()
    context = {
        'posts': Post.objects.filter(publish=True),
        'now': now,
        'otherdate': now + datetime.timedelta(days=0),

    }
    return render(request, 'blog.html', context)


def postingan(request, url):
    post = Post.objects.filter(url=url).first()
    post.views = post.views + 1
    post.save()
    context = {
        'count': 1,
        'post': post,
    }
    return render(request, 'postingan.html', context)
