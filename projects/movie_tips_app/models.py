from django.db import models
from movie_recommender_app.choices import MOVIE_TUPLES, RATING_TUPLES


# Create your models here.
class MovieRecommender(models.Model):
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField(default='No description provided')

    def __str__(self):
        return f'movie recommender id: {self.id} '

    @staticmethod
    def get_by_pk(pk):
        return MovieRecommender.objects.get(id=pk)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class MovieRatings(models.Model):
    movie_recommender_id = models.ForeignKey(MovieRecommender, on_delete=models.CASCADE)
    movie_title_1 = models.CharField(choices=MOVIE_TUPLES, max_length=200)
    rating_1 = models.IntegerField(choices=RATING_TUPLES)
    movie_title_2 = models.CharField(choices=MOVIE_TUPLES, max_length=200)
    rating_2 = models.IntegerField(choices=RATING_TUPLES)
    movie_title_3 = models.CharField(choices=MOVIE_TUPLES, max_length=200)
    rating_3 = models.IntegerField(choices=RATING_TUPLES)
    recommended_movie_1 = models.CharField(max_length=200, default="")
    recommended_movie_2 = models.CharField(max_length=200, default="")
    recommended_movie_3 = models.CharField(max_length=200, default="")
    recommended_movie_4 = models.CharField(max_length=200, default="")
    recommended_movie_5 = models.CharField(max_length=200, default="")

    @staticmethod
    def get_by_pk(pk):
        return MovieRatings.objects.get(id=pk)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
