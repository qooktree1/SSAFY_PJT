import requests
from pprint import pprint


def vote_average_movies():
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
        'api_key': '1f4e35b537297dc83bf23024d8160334',
        'region': 'KR',
        'language': 'ko'
    }
    response = requests.get(BASE_URL+path, params=params).json()

    answer = []
    movie_result = []
    for movie in response.get('results'):
        if movie.get('vote_average') >= 8:
            movie_result.append(movie)
    # return movie_result # --> 영화들의 정보 출력
    for i in movie_result:
        answer.append(i.get('title'))
    return answer


if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
