from django.db import models

# Create your models here.
class User(models.Model):
    """
    Class representing a user or patron of the library

    Variables:
        first_name - The user's first name
        last_name - The user's last name
        email - The user's email address
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)

    class Meta:
        ordering = ["first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class CatalogItem(models.Model):
    """
    Base class representing items in the library catalog

    Variables:
        title - The title of the item in the catalog
        pub_date - The date the item was released or published
        add_date - The date the item was added to the library catalog
        checked_out - A boolean that checks whether or not the item has been checked out
        user - The user that has the item currently checked out (if it is checked out)
    """
    title = models.CharField(max_length=200)
    pub_date = models.DateField("date published")
    add_date = models.DateField("date added")
    checked_out = models.BooleanField(default=False)
    user = models.ManyToManyField(User, blank=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

class Book(CatalogItem):
    """
    Class representing a book. It extends the CatalogItem class and adds an author

    Variables:
        author - The name of the author of the book
    """
    author = models.CharField(max_length=100)

class Game(CatalogItem):
    """
    Class representing a video game. It extends the CatalogItem class and adds a developer

    Variables:
        developer - The name of the developer of the game
    """
    developer = models.CharField(max_length=100)

class Magazine(CatalogItem):
    """
    Class representing a magazine. It extends the CatalogItem class and adds an issue number

    Variables:
        issue - The issue number for that particular magazine
    """
    issue = models.IntegerField(default=1)

class Movie(CatalogItem):
    """
    Class representing a movie. It extends the CatalogItem class and adds a director

    Variables:
        author - The name of the director of the movie
    """
    director = models.CharField(max_length=100)
