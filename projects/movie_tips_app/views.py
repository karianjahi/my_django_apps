from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import MovieRecommender, MovieRatings
from .serializers import MovieRecommenderSerializer, MovieRatingsSerializer, UserSerializer, MovieRatingsDeSerializer, \
    MovieRatingsDetailSerializer, MovieRatingsDeleteSerializer
from movie_recommender_app.permissions import IsOwnerOrReadOnly
from movie_recommender_app.movie_recommender import recommend_movies


# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = User


class MovieRecommenderList(generics.ListCreateAPIView):
    queryset = MovieRecommender.objects.all()
    serializer_class = MovieRecommenderSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MovieRecommenderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieRecommender.objects.all()
    serializer_class = MovieRecommenderSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]


class MovieRatingsList(generics.ListCreateAPIView):
    queryset = MovieRatings.objects.all()
    serializer_class = MovieRatingsSerializer

    # permission_classes = [permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class MovieRatingsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieRatings.objects.all()
    serializer_class = MovieRatingsDetailSerializer

    def get(self, request, pk, *args, **kwargs):
        movies_obj = MovieRatings.objects.get(pk=pk)
        serialized_data = MovieRatingsDetailSerializer(movies_obj).data
        return Response(serialized_data)

    def put(self, request, pk, *args, **kwargs):
        movie_obj = MovieRatings.objects.get(pk=pk)
        data = request.data
        print(data)
        # implement machine learning here
        movies = recommend_movies(data, n=5)
        # End of machine learning implementation

        data["recommended_movie_1"] = movies[0]
        data["recommended_movie_2"] = movies[1]
        data["recommended_movie_3"] = movies[2]
        data["recommended_movie_4"] = movies[3]
        data["recommended_movie_5"] = movies[4]
        serializer = MovieRatingsDeSerializer(movie_obj, data=data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieRatingsDelete(generics.DestroyAPIView):
    queryset = MovieRatings.objects.all()
    serializer_class = MovieRatingsDeleteSerializer
