# pjt09

### 최은우 README

크게 3가지의 단계로 보고 진행하기로 했습니다.

1. 유저 팔로우 기능 - "AJAX통신을 이용하여 서버에서 JSON데이터를 받아와 상황에 맞게 HTML화면 구성"

2. 리뷰 좋아요 기능 - "AJAX통신을 이용하여 서버에서 JSON데이터를 받아와 상황에 맞게 HTML화면 구성"

3. 영화 추천 기능 - 사용자가 인증이 되어있다면 적절한 알고리즘을 활용하여 10개의 영화를 추천 제공

   알고리즘 예시 - 랜덤 / 평균 평점 높은 순서 등



## 1. 

* csrf-token

* 팔로우와 팔로우 취소 버튼을 눌렀을 때 버튼의 값이 바뀌지 않음

  => button태그는 type=submit  ---> form을 제출하긴 하지만 value를 가지지 않음

  ​							type=button ---> form을 제출하지 않음

  => input 태그 type=input ---> form 제출





* 비동기 방식으로 팔로우와 팔로우 취소, 팔로워와 팔로잉 숫자를 바꿔주기 위해 AJAX통신을 이용했음
* axios를 사용하여 promise방식으로 구현하였음
  * `isFollowed`: 팔로우 한 상태인지 확인하기 위한 변수
  * `followerCount`: 팔로워 수를 세기 위한 변수
  * `followinsCount`: 팔로잉 수를 세기 위한 변수



## 2.

1번과 비슷한 방식으로 AJAX를 이용하여 구현

1번과는 다르게 여러 게시글에 좋아요를 누를 수 있는 상황이므로 querySelectorAll() 을 사용

* 이 때 프로필 페이지로 넘어갈 때 addEventListener를 인식할 수 없는 에러가 계속해서 발생

  * `const form = document.querySelector('#follow-form')` 이 부분에서 form이 null값이기 때문에 당연히 addEventListener를 인식할 수 없는 상황이였음

    => `form.addEventListener`부분부터 `if (form != null) {`로 감싸서 해결

    ```javascript
    if (form != null) {
    
          form.addEventListener('submit', function (event) {
            event.preventDefault()
      
            
            const userId = event.target.dataset.id
            const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
      
            axios({
              method: 'post',
              url: `http://127.0.0.1:8000/accounts/${userId}/follow/`,
              headers: {'X-CSRFToken': csrftoken},
            })
              .then(response => {
                const isFollowed = response.data.is_followed
                const followBtn = document.querySelector('#follow-input')
                const followCountDiv = document.querySelector('#follow-count')
                const followersCount = response.data.followers_count
                const followingsCount = response.data.followings_count
      
                if(isFollowed === true) {
                  followBtn.value = '언팔로우'
                } else {
                  followBtn.value = '팔로우'
                }
                
      
                followCountDiv.innerText = `팔로잉 수 : ${followingsCount} / 팔로워 수 : ${followersCount}`
              })
            
              .catch(error => {
                console.log(error)
              })
          })
        }
    ```

    

## 3. 영화 추천

앞선 1, 2번에서 예기치 못한 에러들 때문에 시간 여유가 없었음ㅠㅠ

따라서 그냥 랜덤해서 10개를 추천하는 방식으로 구현하기로 함

```python
@require_safe
def recommended(request):
    movies = Movie.objects.all()
    movie_random = random.sample(list(movies), 10)
    context = {
        'movie_random': movie_random,
    }
    return render(request, 'movies/recommended.html', context)
```

* views.py 에서 recommended부분은 위 코드 처럼 구현

  * 먼저 movie데이터를 모델을 통해 받은 후 random 모듈을 통해 10개만 선택 후 인자로 넘김

    여기서 random으로 선택 할 때 movies는 json 즉, dictionary형태이므로 list로 바꿔서 받아줘야 함

```django
{% extends 'base.html' %}


{% block content %}
<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3  row-cols-lg-4 d-flex justify-content-center">
  {% for movie in movie_random %}
  
  <div class="card" style="width: 18rem;">
      <img class="card-img-top" src="{{movie.poster_path}}" alt="Card image cap">
    <div class="card-body">
      <h5 class="card-title"><strong>영화제목</strong> {{ movie.title }}</h5>

      <p class="card-text"
      style="overflow: hidden; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical;">내용: {{ movie.overview }}</p>

      <p class="card-text">vote_average: {{ movie.vote_average }}</p>
      <p class="card-text">장르: {{ movie.genre }}</p>
      <p class="card-text">개봉일: {{ movie.release_date }}</p>
        
    </div>
  </div>

  {% endfor %}
</div>
{% endblock %}
```

django html부분은 위의 코드처럼 구현 함

for문을 통해 영화 정보를 하나씩 받고 각 영화 정보를 카드 섹션으로 만들었습니다.



------

------

# 김신철 README

# 오늘의 배움

1. accounts/profile.html

   JS 안에서 addEventListener는 자동으로 로드가 되고, submit이 될때를 기다리는데 이것을 생각하지 않고, submit이 되지 않으면 코드는 무시된다고 생각함.

   => 여기서 addEventListener가 로드되지 않도록 처음부터 조건식을 걸어야 함. (addEventListener의 작동 방식을 잘못 알고 있었음)

   ```html
    <script>
       
       const form = document.querySelector('#follow-form')
       if (form != null) {
   
         form.addEventListener('submit', function (event) {
           event.preventDefault()
     
           
           const userId = event.target.dataset.id
           const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value
     
           axios({
             method: 'post',
             url: `http://127.0.0.1:8000/accounts/${userId}/follow/`,
             headers: {'X-CSRFToken': csrftoken},
           })
             .then(response => {
               const isFollowed = response.data.is_followed
               const followBtn = document.querySelector('#follow-input')
               const followCountDiv = document.querySelector('#follow-count')
               const followersCount = response.data.followers_count
               const followingsCount = response.data.followings_count
     
               if(isFollowed === true) {
                 followBtn.value = '언팔로우'
               } else {
                 followBtn.value = '팔로우'
               }
               
     
               followCountDiv.innerText = `팔로잉 수 : ${followingsCount} / 팔로워 수 : ${followersCount}`
             })
           
             .catch(error => {
               console.log(error)
             })
         })
       }
     </script>
   ```

   axios 안에서 정보를 바꿀 때, 직접 해당 값에 접근하여 일일이 바꾸는 방법과 setAttribute를 통해 변경하는 방법이 있다.

   ```html
               if(isFollowed === true) {
                 followBtn.value = '언팔로우'
               } else {
                 followBtn.value = '팔로우'
               }
   ```

   ```html
               if (isLiked === true) {
                 heart.setAttribute('style', 'color:red')
               } else {
                 heart.setAttribute('style', 'color:black')
               }
   ```

   

2. movies/recommended.html

   정보를 받아서 for문 안에서 하나의 요소들 각각을 카드에 넣는 것을 익힘

   ```html
   <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3  row-cols-lg-4 d-flex justify-content-center">
     {% for movie in movie_random %}
     
     <div class="card" style="width: 18rem;">
         <img class="card-img-top" src="{{movie.poster_path}}" alt="Card image cap">
       <div class="card-body">
         <h5 class="card-title"><strong>영화제목</strong> {{ movie.title }}</h5>
   
         <p class="card-text"
         style="overflow: hidden; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical;">내용: {{ movie.overview }}</p>
   
         <p class="card-text">vote_average: {{ movie.vote_average }}</p>
         <p class="card-text">장르: {{ movie.genre }}</p>
         <p class="card-text">개봉일: {{ movie.release_date }}</p>
           
       </div>
     </div>
   ```

   

3. movies/views.py

   Movie.objects.all()로 쿼리셋을 받고 이를 리스트로 변환하여 random 모듈로 10개 요소를 추출한다.

   => 쿼리셋으로는 원하는 정보에 접근할 수 없으므로 접근 가능한 형태로 변환

   ```python
   @require_safe
   def recommended(request):
       movies = Movie.objects.all()
       movie_random = random.sample(list(movies), 10)
       context = {
           'movie_random': movie_random,
       }
       return render(request, 'movies/recommended.html', context)
   ```

   

   ------

   ------


# 박종민 README

# 관통 프로젝트 2022-05-06 [pjt09]

### 목적

- 데이터를 생성, 조회, 수정, 삭제할 수 있는 Web Application 제작
- AJAX 통신과 JSON 구조에 대한 이해
- Database 1:N, M:N 관계의 이해와 데이터 관계 설정
- 영화 추천 알고리즘 설계



### 준비사항

#####  언어

- Python 3.9+
- Django 3.2+

#####  도구

- Visual Studio Code
- Chrome Browser

---

### New code 수정사항 - movies

- `recommended.html`

  ```django
  {% extends 'base.html' %}
  
  
  {% block content %}
  <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3  row-cols-lg-4 d-flex justify-content-center">
    {% for movie in movie_random %}
    
    <div class="card" style="width: 18rem;">
        <img class="card-img-top" src="{{movie.poster_path}}" alt="Card image cap">
      <div class="card-body">
        <h5 class="card-title"><strong>영화제목</strong> {{ movie.title }}</h5>
  
        <p class="card-text"
        style="overflow: hidden; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical;">내용: {{ movie.overview }}</p>
  
        <p class="card-text">vote_average: {{ movie.vote_average }}</p>
        <p class="card-text">장르: {{ movie.genre }}</p>
        <p class="card-text">개봉일: {{ movie.release_date }}</p>
          
      </div>
    </div>
  
    {% endfor %}
  </div>
  {% endblock %}
  ```

- 내용이 긴 글의 글을 줄이기 위하여 css `-webkit-box`, `-webkit-line-clamp`, `-webkit-box-orient` 속성을 사용함

- `Webkit` : **웹 브라우저를 만드는 데 기반을 제공하는 오픈 소스 응용 프로그램 프레임워크**

- `-webkit-은 크롬과 사파리가 채용한 웹 브라우저 엔진 이름`

  - `-webkit-line-clamp` :  **블록 컨테이너의 콘텐츠를 지정한 줄 수만큼으로 제한**

  - `-webkit-box-orient` : **flexible box의 흐름방향을 지정하는 속성**

    - **vertical , horizontal을 지정하여 사용**

      

## New Learned & Problems

- JavaScript를 addEventListener 를 이용한 AJAX 통신을 구현하는 과정에서 어느 부분을 더하고 빼는지 확실치 않아 시간이 오래 걸리며 시행착오를 겪으며 코드를 짰습니다.


   - View함수에서 어떤 값을 Json 데이터 형태로 넘겨줘야하는지 생각해보게 되는 시간을 가지며 어떤 html tag 위치에서 클래스 및 아이디에 속성을 넣어야 하는지 알게 되었습니다.

   

   - Recommendend 페이지에서는 DB에 저장되어 있는 영화 목록 중 무작위 10개를 Bootstrap Card 안의 형태로 나타냄
   - ManyToMany 의 속성을 잊어버린 것 같아 외래키로 접근해야 하는 장르를 제 시간내에 작성하지 못하였다.


---

   # 프로젝트 총평

   - 복습하자.
