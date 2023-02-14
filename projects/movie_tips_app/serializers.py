from .models import MovieRecommender, MovieRatings, Recommendations
from rest_framework import serializers
from django.contrib.auth.models import User


class MovieRecommenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRecommender
        fields = ["owner", "name", "created_on", "description"]


class MovieRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRatings
        fields = [
            "movie_recommender_id",
            "movie_title_1",
            "rating_1",
            "movie_title_2",
            "rating_2",
            "movie_title_3",
            "rating_3",
        ]


class RecommendationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recommendations
        fields = [
            "movie_1",
            "movie_2",
            "movie_3",
            "movie_4",
            "movie_5",
        ]


class UserSerializer(serializers.ModelSerializer):
    movie_recommender = serializers.PrimaryKeyRelatedField(many=True,
                                                           queryset=MovieRecommender.objects.all())

    class Meta:
        model = MovieRecommender
        fields = [
            "id",
            "username",
            "movie_recommender"
        ]
