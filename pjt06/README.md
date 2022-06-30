# 관통 프로젝트 2022-04-08 [pjt06]

# 과정

- 가상환경 생성
- 가상환경 활성화 후 패키지 목록 설치 with requirements.txt
- `.gitignore` 작성
- 프로젝트 생성
- 앱 생성
- urls.py
- views.py
- models.py
  - `CharField`, `IntegerField`, `DateField`, `FloatField`, `TextField` 사용
  - `title`, `genre ` 는 `CharField(max_length)` 를 사용하여 최대값 설정
  - `audience` : `IntegerField` 사용
  - `release_date` : `DateField` 사용
  - `score` : `FloatField` 사용
  - `poster_url`, `description` : `TextField` 사용

- templates
- forms.py
- admin.py

### 목적

- 데이터를 생성, 조회, 수정, 삭제 가능한 웹 어플리케이션
- Django `ModelForm`을 활용한 사용자 요청 데이터 `유효성 검증`

---

#### urls.py

- `index` : 전체 영화 목록 페이지 조회
- `create` : 영화 작성 페이지 조회 & 단일 영화 데이터 저장
- `detail` : 단일 영화 상세 페이지 조회
- `update` : 영화 수정 페이지 조회 & 단일 영화 데이터 수정
- `delete` : 단일 영화 데이터 삭제

----

#### admin.py

- admin 등록
- `list_display`
  - models.py에 정의한 column 들의 값을 admin 페이지에 출력

- 로그인 정보
  - Username : `movies`
  - Email address : `qooktree@naver.com`
  - Password : 1234


----------------------------------------------------------------------------------------------------------

#### views.py

- index

  - `@require_safe`
    - GET, HEAD method만 허용하도록 함

  - `order_by('-pk')` : 최신글을 위에 두기

  

- create

  - `@require_http_methods(['GET', 'POST'])`

    - GET, POST method 요청만 승인하도록 함

  - Method 분류

    - POST일 경우
      - 유효성 검사 성공 -> 입력받은 form(date 포함) 을 DB에 저장 -> detail page로 이동
        - `movie` 객체의 기본키를 통해 detail page 접근

      - 유효성 검사 실패 -> 입력받은 form(data 포함) 을 인자로 render

    - GET일 경우
      - form 을 인자로 render


​    

  - detail

    - `@require_safe`
      - GET, HEAD method만 허용하도록 함
      

    - 해당하는 영화의 값들을 DB에 접근하여 render


​    

  - update
    - `@require_http_methods(['GET', 'POST'])`
      - GET, POST method 요청만 승인하도록 함
    - Method 분류
      - POST일 경우
        - 입력되어 있는 정보를 form에 저장

          - 유효성 검사 성공

            - 수정한 정보를 form 객체를 DB에 -> detail page로 이동

          - 유효성 검사 실패

            - 입력되어 있는 정보를 가지고 update page에 재접근
        - GET일 경우

          - 입력되어 있는 정보를 인자로 가지고 render



​      

  - delete
    - `@require_POST()`
      - POST method 요청만 승인하도록 함
    - 해당하는 tuple(데이터)을 삭제


---

#### Templates

- index.html

  - CREATE URL -> 영화 정보 삽입 가능

  - 영화 제목과 평점을 보여줌

    - for문을 사용하여 table에 추가, 삭제, 업데이트 될때마다 반영

  - 영화 제목을 클릭하면 그 영화에 대한 정보를 보여줄 detail page 이동
  
    
  


- detail.html

  - 영화의 정보들을 출력(Title, Audience, Release Dates, Genre, Content)
  - `DELETE`, `UPDATE`, `BACK(인덱스로 이동)` 할 수 있음



- create.html

  - `bootstrap_form` 사용

    ```django
    <form action="{% url 'movies:create' %}" method="POST">
        {% csrf_token %}
    
        {% bootstrap_form form %}
        {% buttons submit='Submit' %}{% endbuttons %}
      </form>
    ```


- update.html

  - pk 값을 받아 선택한 영화의 정보를 그대로 받아 수정할 수 있게 함
  - create.html 와 같이 `bootstrap_form` 사용



---

#### Form

- audience, genre, score, release_date 에 widget 추가

  - audience

    - `IntegerField(NumberInput, )`, type = 'number', min = 0(관객수는 0명 미만으로 내려갈 수 없음)

  - genre

    - `ChoiceField(Select, )`, choices = ['코미디', '공포', '로맨스']

  - score

    - `FloatField(NumberInput, )`, type = 'number', min = 0, max = 5, step = 0.5

  - release_date

    - `DateField(DateInput, )`, type = 'date'

    

- Meta class(ModelForm)
  - 모든 필드 사용



---

## New Learned & Problems

- CRUD 를 코드로 구현하는 부분은 문제가 안되지만 Form 이나 ModelForm을 이용하여 CRUD 를 만드는 것이 어려워 필기하였던 Notion을 이용하여 구현하였습니다.

  - ModelForm or Form 에 익숙해지기 위해 여러번 반복하며 짤 것입니다.

    

- forms.py 에서 widget을 설정하는 부분을 새롭게 배웠습니다.

  

- input format의 `number type`일때 min을 minlength, max를 maxlength로 설정하여 안되는 구간이 있어 시간이 걸렸습니다. 다행히 `forms.py` 를 처음부터 다시 보면서 조금이라도 헷갈리는 부분은 `Django 공식문서` 와 `stackoverflow` searching을 하며 찾아보았습니다.

  

---

# 프로젝트 총평

- `Form & ModelForm`

  - **CRUD 시스템을 Form 과 ModelForm 을 이용하여 짜보는 연습을 하자**

    

- 유효성 검사를 할때를 고려하여 경고 메시지나 Image를 창에 띄울지 띄우지 않을 지 결정하는 코드를 짜보는 연습을 하자
