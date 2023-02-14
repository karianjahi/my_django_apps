from .models import UserMovie
from rest_framework import serializers
from django.contrib.auth.models import User

 

class UserMovieSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = UserMovie
        fields = ["id", 
                  "name", 
                  "description", 
                  "created_on", 
                  "created_by",
                  "movie_title_1", 
                  "rating_1", 
                  "movie_title_2", 
                  "rating_2", 
                  "movie_title_3", 
                  "rating_3",
                  "owner", 
                #   "recommended_movie_1",
                #   "recommended_movie_2",
                #   "recommended_movie_3",
                  ]
        

class UserMovieDeSerializer(serializers.ModelSerializer):
    created_by = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = UserMovie
        fields = ["id", 
                  "name", 
                  "description", 
                  "created_on", 
                  "created_by",
                  "recommended_movie_1",
                  "recommended_movie_2",
                  "recommended_movie_3",
                  ]
        

class UserSerializer(serializers.ModelSerializer):
    movies = serializers.PrimaryKeyRelatedField(many=True, queryset=UserMovie.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'movies']