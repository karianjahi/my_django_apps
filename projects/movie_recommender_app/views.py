from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import UserMovie
from .serializers import UserMovieSerializer, UserSerializer, UserMovieDeSerializer
from .permissions import IsOwnerOrReadOnly
from .movie_recommender import recommend_movies

class UserMovieList(generics.ListCreateAPIView):
    queryset = UserMovie.objects.all()
    serializer_class = UserMovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class UserMovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserMovie.objects.all()
    serializer_class = UserMovieSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    def get(self, request, pk, *args, **kwargs):
        usermovie = UserMovie.objects.get(pk=pk)
        serialized_data = UserMovieDeSerializer(usermovie).data
        return Response(serialized_data)
    
    def put(self, request, pk, *args, **kwargs):
        # print(request.data, pk)
        user_movie = UserMovie.objects.get(pk=pk)
        
        """ 
        Implement recommendations at put request and save the data to the database
        """
        data = request.data
        movies = recommend_movies(data)
        data["recommended_movie_1"] = movies[0]
        data["recommended_movie_2"] = movies[1]
        data["recommended_movie_3"] = movies[2]
     

        serializer = UserMovieDeSerializer(user_movie, data=data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            # print(serialized_data)
            return Response(serialized_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
        
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer     



