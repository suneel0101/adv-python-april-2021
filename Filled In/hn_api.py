import requests

CACHE_DATABASE = {'data': None}

def get_top_stories():
    if CACHE_DATABASE['data'] is None:
        CACHE_DATABASE['data'] = requests.get(
            'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty').json()
    return CACHE_DATABASE['data']