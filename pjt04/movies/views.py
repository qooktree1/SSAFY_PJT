from django.shortcuts import render
import requests
import random
API_KEY = '1f4e35b537297dc83bf23024d8160334'
BASE_URL = "https://api.themoviedb.org/3"
IMG_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_URL = "https://themoviedb.org/movie/"

def index(request):
    path = '/movie/top_rated'
    params = {
        'api_key' : API_KEY,
        'region' : 'KR',
        'language' : 'ko',
    }
    response = requests.get(BASE_URL+path, params=params).json()
    m_id = []
    title = []
    overview = []
    release_date = []
    poster_path = []
    backdrop_path = []

    for i in response.get('results'):
        m_id.append(i.get('id'))
        poster_path.append(i.get('poster_path'))
        title.append(i.get('title'))
        overview.append(i.get('overview'))
        release_date.append(i.get('release_date'))
        backdrop_path.append(i.get('backdrop_path'))

    movie_len = len(m_id)
    numbers = []
    selected_numbers = []
    for i in range(movie_len):
        numbers.append(i)
    selected_numbers = random.sample(numbers, 6)
    r_m_id = []
    r_poster_path = []
    r_title = []
    r_overview = []
    r_release_date = []
    r_backdrop_path = []
    for i in selected_numbers:
        r_m_id.append(m_id[i])
        r_poster_path.append(poster_path[i])
        r_title.append(title[i])
        r_overview.append(overview[i])
        r_release_date.append(release_date[i])
        r_backdrop_path.append(backdrop_path[i])
    images = []
    back_images = []
    for i in range(6):
        images.append(IMG_URL + r_poster_path[i])
        back_images.append(IMG_URL + r_backdrop_path[i])

    content = {
        'title' : r_title,
        'overview' : r_overview,
        'release_date' : r_release_date,
        'images' : images,
        'm_id' : r_m_id,
        'back_images' : back_images,
    }
    return render(request, 'index.html', content)


def recommendations(request):
    
    base_title = "쇼생크 탈출"
    movie_id = 0
    path = '/search/movie'
    params = {
        'api_key' : API_KEY,
        'region' : 'KR',
        'language' : 'ko',
        'query' : base_title,
    }
    response = requests.get(BASE_URL+path, params=params).json()
    for i in response.get('results'):
        movie_id = i.get('id')
    
    # 영화 정보들 선언
    m_id = []
    title = []
    vote_average = []
    overview = []
    release_date = []
    poster_path = []

    new_response = requests.get(f'{BASE_URL}/movie/{movie_id}/recommendations',params=params).json()
    for i in new_response.get('results'):
        m_id.append(i.get('id'))
        poster_path.append(i.get('poster_path'))
        title.append(i.get('title'))
        vote_average.append(i.get('vote_average'))
        overview.append(i.get('overview'))
        release_date.append(i.get('release_date'))
    rand_len = len(title)
    num = random.randrange(rand_len)

    content = {
        'm_id' : MOVIE_URL + str(m_id[num]),
        'poster_path' : IMG_URL + poster_path[num],
        'title' : title[num],
        'vote_average' : vote_average[num],
        'overview' : overview[num],
        'release_date' : release_date[num],
    }
    
    return render(request, 'recommendations.html', content)