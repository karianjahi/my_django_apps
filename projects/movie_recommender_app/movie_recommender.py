import random
from .choices import MOVIES


def recommend_movies(put_request_dict):
    random.shuffle(MOVIES)
    return MOVIES[:3]

print(recommend_movies(""))