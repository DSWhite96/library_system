from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Book, CatalogItem, Game, Magazine, Movie, User
from .serializer import BookSerializer, CatalogItemSerializer, GameSerializer, MagazineSerializer, MovieSerializer, UserSerializer

@api_view(['GET'])
def get_books(request):
    books = Book.objects.all()
    serializedData = BookSerializer(books, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def get_catalog_items(request):
    catalog_items = CatalogItem.objects.all()
    serializedData = CatalogItemSerializer(catalog_items, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def get_games(request):
    games = Game.objects.all()
    serializedData = GameSerializer(games, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def get_magazines(request):
    magazines = Magazine.objects.all()
    serializedData = MagazineSerializer(magazines, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    serializedData = MovieSerializer(movies, many=True).data
    return Response(serializedData)

@api_view(['GET'])
def get_users(request):
    users = User.objects.all()
    serializedData = UserSerializer(users, many=True).data
    return Response(serializedData)
