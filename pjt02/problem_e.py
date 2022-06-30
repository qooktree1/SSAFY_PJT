import requests
from pprint import pprint


def credits(title):
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
        'api_key': '1f4e35b537297dc83bf23024d8160334',
        'region': 'KR',
        'language': 'ko',
        'query': title
    }
    response = requests.get(BASE_URL+path, params=params).json()

    movie_id = 0
    for search in response.get('results'):
        movie_id = search.get('id')

    new_response = requests.get(
        f'{BASE_URL}/movie/{movie_id}/credits', params=params).json()

    if new_response.get('cast') == None:
        return None

    actor_list = []
    director_list = []
    result = {}
    for i in new_response.get('cast'):
        if i.get('cast_id') < 10:
            actor_list.append(i.get('name'))

    for j in new_response.get('crew'):
        if j.get('known_for_department') == 'Directing':
            director_list.append(j.get('name'))

    result = {'cast': actor_list, 'crew': director_list}
    return result


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
