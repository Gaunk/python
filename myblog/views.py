from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Post, Author, ListHarga, TempatKursus, JoinField
import pytz
from datetime import datetime
import datetime
# Create your views here.


def home(request):
    biaya = ListHarga.objects.all()

    # biaya = ListHarga.objects.all()
    now = datetime.datetime.now()
    context = {'biaya': biaya,
               'now': now,
               'otherdate': now + datetime.timedelta(days=0),
               }
    return render(request, 'base_code.html', context)


def blog(request):
    # tempatkursus = TempatKursus.objects.create()
    posts = Post.objects.all()
    now = datetime.datetime.utcnow()
    context = {
        'kursus': TempatKursus.objects.all(),
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
