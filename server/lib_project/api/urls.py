from django.urls import path
from .views import get_books, get_catalog_items, get_games, get_magazines, get_movies, get_users

urlpatterns = [
    path('books/', get_books, name='get_books'),
    path('catalog/', get_catalog_items, name='get_catalog_items'),
    path('games/', get_games, name='get_games'),
    path('magazines/', get_magazines, name='get_magazines'),
    path('movies/', get_movies, name='get_movies'),
    path('users/', get_users, name='get_users'),
]