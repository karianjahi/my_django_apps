from django.urls import path
from movie_tips_app import views
urlpatterns = [
    path('movie_home_page/', views.MovieRecommenderList.as_view(), name="all_entries"),
    path('movie_home_page/<int:pk>/', views.MovieRecommenderDetail.as_view(), name="single_entry"),

    path('movie_home_page/chosen_movies/', views.MovieRatingsList.as_view(), name="all_chosen_movies"),
    path('movie_home_page/chosen_movies/<int:pk>/', views.MovieRatingsDetail.as_view(), name="single_chosen_session"),

    path('movie_home_page/recommended_movies/', views.RecommendationsList.as_view(), name="all_recommended_movies"),
    path('movie_home_page/recommended_movies/<int:pk>/', views.RecommendationsDetail.as_view(), name="single_recommended_session"),

]

