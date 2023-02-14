from django.db import models
from .choices import RATING_TUPLES, MOVIE_TUPLES

# Create your models here.

class UserMovie(models.Model):
    name = models.TextField(default="movies")
    description = models.TextField(default="Recommending movies")
    created_on = models.DateTimeField(auto_now_add=True)
    movie_title_1 = models.CharField(choices=MOVIE_TUPLES, max_length=200)
    rating_1 = models.IntegerField(choices=RATING_TUPLES)
    movie_title_2 = models.CharField(choices=MOVIE_TUPLES, max_length=200)
    rating_2 = models.IntegerField(choices=RATING_TUPLES)
    movie_title_3 = models.CharField(choices=MOVIE_TUPLES, max_length=200)
    rating_3 = models.IntegerField(choices=RATING_TUPLES)
    owner = models.ForeignKey('auth.User', related_name='movie', on_delete=models.CASCADE)
    recommended_movie_1 = models.CharField(blank=True, max_length=200)
    recommended_movie_2 = models.CharField(blank=True, max_length=200)
    recommended_movie_3 = models.CharField(blank=True, max_length=200)
    class Meta:
        ordering = ['movie_title_1', 
                    'rating_1', 
                    'movie_title_2', 
                    'rating_2', 
                    'movie_title_3', 
                    'rating_3']
    
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        super().save(*args, **kwargs)
    

    

    

    
