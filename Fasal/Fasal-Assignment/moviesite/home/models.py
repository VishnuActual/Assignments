# models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    ratings_imdb = models.DecimalField(max_digits=3, decimal_places=1)
    ratings_rotten_tomatoes = models.PositiveSmallIntegerField()
    ratings_metacritic = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=50)
    movie_type = models.CharField(max_length=50)
    star = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    singers = models.CharField(max_length=200)
    picture_address = models.CharField(max_length=200)

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie')

    class Meta:
        unique_together = ('user', 'movie')


    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'
