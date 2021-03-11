from django.db import models
from django.contrib.auth.models import User
from joinfield.joinfield import JoinField
# Create your models here.


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user}'


class Kategori(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class PilihanHarga(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class ListHarga(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=3)
    halaman = models.CharField(max_length=100)
    biaya_setup = models.CharField(max_length=50)
    hosting = models.CharField(max_length=50)
    maintenance = models.TextField()
    tambahan = models.TextField()
    domain = models.TextField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_upload = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img')
    publish = models.BooleanField()
    kategori = models.ManyToManyField(Kategori)
    views = models.IntegerField(default=0)
    url = models.CharField(("myblog_post.urls"), max_length=50)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title


class TempatKursus(models.Model):
    title = models.CharField(max_length=50)
    t_content = models.CharField(max_length=150)
    t_img = models.ImageField(upload_to='img')
    time_up = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
