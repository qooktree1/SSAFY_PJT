import requests
from pprint import pprint


def ranking():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '1f4e35b537297dc83bf23024d8160334',
        'region': 'KR',
        'language': 'ko'
    }
    response = requests.get(BASE_URL+path, params=params).json()

    movie_result = []
    result = []
    for movie in response.get('results'):
        movie_result.append(movie)

    for i in range(len(movie_result)-1):
        for j in range(i+1, len(movie_result)):
            if movie_result[i].get('vote_average') < movie_result[j].get('vote_average'):
                movie_result[i], movie_result[j] = movie_result[j], movie_result[i]

    for i in range(5):
        result.append(movie_result[i])
    return result


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
