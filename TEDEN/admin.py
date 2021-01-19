from django.contrib import admin
from .models import Book, Author, Language, Genre
# Register your models here.


admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)