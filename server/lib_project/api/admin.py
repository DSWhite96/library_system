from django.contrib import admin
from .models import CatalogItem, Book, Game, Magazine, Movie, User

# Register your models here.
admin.site.register([CatalogItem, Book, Game, Magazine, Movie, User])