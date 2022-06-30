# 7기 관통 프로젝트 2022-01-28 [pjt02]

# Problem!

- problem_a.py

  ```python
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
  
  ```

  - Youtube 온라인 강의때 필기한 것들에 많은 도움이 있었다
  - requests를 이용해 url 과 params(api_key, ..) 를 json파일 형태로 response에 저장
  - 후 results안의 영화 데이터에서 딕셔너리 파트마다 count값을 올려줘 영화목록의 개수를 구하였다
  - 처음에는 .get('results')를 사용하지 않아 object들의 개수만 나온다
    - 문제에 대해 신중히 풀어보는 실력을 갖춰야겠다

- problem_b.py

  ```python
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
  
  ```

  - movie_result에 vote_average가 8이상인 dict를 append한 후 

    answer 리스트에 영화제목들을 append하였다

  - 막히는 부분은 없었다

- problem_c.py

  ```python
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
  ```

  - 2중 for문을 이용해 접근한 케이스
    - 인덱스로 접근하여 i 와 다음 항목(j)를 검사하여 vote_average가 큰 영화정보가 리스트의 앞으로 가게 했다
    - 처음에 max_ 변수를 설정하여 max_ 와 vote_average를 비교하는 접근법으로 갔지만 해결이 나지 않아 2중 for문으로 푼 case
  - 후 for문을 5번 순환하게 하여 가장 높은 평점을 가진 데이터만 result값에 append 했다

- problem_d.py

  ```python
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
  ```

  - 처음에 문제의 의미를 이해하지 못하여 방황했다
    - query에 id를 넣어서 문제를 풀지 못하였고 다른 문제를 둘러보다 발견하여 바꾸게 됐다
    - `url, path, params, requests 관계를 다시 복습하여 개념을 숙지해야 한다`
  - movie_id에 id 값을 받아온 후 다음 (Get  Recommendations) URL을 생성할때 사용했다
  - new_response.get('results') == None을 통해 추천 영화가 없는 것을 표현했다
    - print문을 사용하여 어디서 영화제목을 찾지 못하는건지 확인해보고 new_response를 받아올때 라는 것을 안 후 짠 코드이다.

- problem_e.py

  ```python
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
  
  ```

  - d 문제를 푼 후 쉽게 접근한 문제이다.
  - 출력 값에 배우리스트와 감독리스트 둘 다 출력하게 되는데 이것을 cast 와 crew 어디서 가져와야 하는지 혼동이와 시간이 조금 걸렸던 문제이다.
    - for문을 이용하여 cast 와 crew 각각 따로 이름을 받아 마지막 result 리스트에 dictionary 형태로 출력하게 만들었다.

# 프로젝트 총평

- **문제를 풀때 이 문제가 어떤 것을 요구하고 그것을 어떻게 풀어 나갈 것인지 생각해 보자**
  - 항상 같은 문제이지만 전 보다 발전된 모습이 좋다
- `조금이라도 걸리는 문제는 다음 문제를 풀어보는 것도 나쁘지 않다`
  - 막혔던 문제를 계속 꽁꽁 싸매서 푸는 것 보다 다른 문제를 풀다가 방법이 생각이 나 푼 문제가 몇 있다
- requests를 이용해서만 풀었기 때문에 bs4를 이용해 풀어봐야겠다
- `끝나고 코드를 공유하며 다른 사람들은 어떤식으로 효율성 있게 풀었는지 확인해보자`

- 지난 번 1차 관통 프로젝트보다 나은 결과물인 것 같아 기쁘다

# 한 줄 결론!

`코드 공유를 통해 내가 사용할 수 있는 방법을 늘려보자!`