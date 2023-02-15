import random
from .choices import MOVIES


def recommend_movies(put_request_dict, n=3):
    random.shuffle(MOVIES)
    return MOVIES[:n]


print(recommend_movies(""))
