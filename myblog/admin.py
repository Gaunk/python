from django.contrib import admin
from .models import Post, Author, Kategori, ListHarga, PilihanHarga, TempatKursus

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Kategori)
admin.site.register(ListHarga)
admin.site.register(PilihanHarga)
admin.site.register(TempatKursus)
