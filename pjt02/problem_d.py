import requests
from pprint import pprint


def recommendation(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '1f4e35b537297dc83bf23024d8160334',
        'region': 'KR',
        'language': 'ko',
        'query': title
    }
    response = requests.get(BASE_URL+path, params=params).json()

    result = []
    movie_id = 0
    for search in response.get('results'):
        movie_id = search.get('id')

    new_response = requests.get(
        f'{BASE_URL}/movie/{movie_id}/recommendations', params=params).json()

    if new_response.get('results') == None:
        return None

    for search2 in new_response.get('results'):
        result.append(search2.get('title'))
    return result


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
