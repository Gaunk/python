from django.db import models
from django.contrib.auth.models import User
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


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    time_upload = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='img')
    publish = models.BooleanField()
    kategori = models.ManyToManyField(Kategori)
    read = models.IntegerField(default=0)
    url = models.CharField(("myblog_post.urls"), max_length=50)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return self.title
