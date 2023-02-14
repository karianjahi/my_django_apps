import pandas as pd
MOVIES = list(pd.read_csv("movie_recommender_app/ml-latest-small/movies.csv", sep=",")["title"])

RATING_CHOICES = [1, 2, 3, 4, 5]

MOVIE_TUPLES = []
for movie in MOVIES:
    MOVIE_TUPLES.append((movie, movie))
    
RATING_TUPLES = []
for rating in RATING_CHOICES:
    RATING_TUPLES.append((rating, rating))
    

    
    
    