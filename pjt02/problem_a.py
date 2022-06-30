from msilib import datasizemask
import requests
from pprint import pprint


def popular_count():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '1f4e35b537297dc83bf23024d8160334',
        'region': 'KR',
        'language': 'ko'
    }
    response = requests.get(BASE_URL+path, params=params).json()
    count = 0
    for i in response.get('results'):
        count += 1
    return count


if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
