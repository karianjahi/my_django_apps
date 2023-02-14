from django.urls import path
from movie_recommender_app import views

urlpatterns = [
    path('recommend_movies/', views.UserMovieList.as_view(), name="all_recommend_movies"),
    path('recommend_movies/<int:pk>/', views.UserMovieDetail.as_view(), name="single_recommende_movie"),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]   