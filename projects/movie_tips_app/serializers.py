from .models import MovieRecommender, MovieRatings
from rest_framework import serializers
from django.contrib.auth.models import User


class MovieRecommenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRecommender
        fields = [
            "id",
            "owner",
            "name",
            "description",
            "created_on",
        ]


class MovieRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRatings
        fields = [
            "id",
            "movie_recommender_id",
            "movie_title_1",
            "rating_1",
            "movie_title_2",
            "rating_2",
            "movie_title_3",
            "rating_3",
            # "recommended_movie_1",
            # "recommended_movie_2",
            # "recommended_movie_3",
            # "recommended_movie_4",
            # "recommended_movie_5",
        ]


class MovieRatingsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRatings
        fields = [
            "id",
            "movie_recommender_id",
            "movie_title_1",
            "rating_1",
            "movie_title_2",
            "rating_2",
            "movie_title_3",
            "rating_3",
            "recommended_movie_1",
            "recommended_movie_2",
            "recommended_movie_3",
            "recommended_movie_4",
            "recommended_movie_5",
        ]


class MovieRatingsDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRatings
        fields = "__all__"


class MovieRatingsDeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieRatings
        fields = [
            "id",
            # "movie_recommender_id",
            "recommended_movie_1",
            "recommended_movie_2",
            "recommended_movie_3",
            "recommended_movie_4",
            "recommended_movie_5",
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
