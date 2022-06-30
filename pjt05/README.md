# 7기 관통 프로젝트 2022-03-11 [pjt05]

# 과정

- 가상환경 생성

- 가상환경 활성화 후 패키지 목록 설치 with requirements.txt

- `.gitignore` 작성

- 프로젝트 생성

- 앱 생성

- `models.py` 수정

  - `CharField`, `IntegerField`, `DateField`, `FloatField`, `TextField` 사용

  - `title`, `genre ` 는 `CharField(max_length)` 를 사용하여 최대값 설정

  - `audience` : `IntegerField` 사용

  - `release_date` : `DateField` 사용

  - `score` : `FloatField` 사용

  - `poster_url`, `description` : `TextField` 사용

    

  - `makemigrations` 입력

  - `migrate` 입력

    

- `urls.py` -> `views.py` -> `templates`

---

#### urls.py

- `index` : 전체 영화 목록 페이지 조회
- `new` : 새로운 영화 작성 페이지 조회
- `create` : 단일 영화 데이터 저장
- `detail` : 단일 영화 상세 페이지 조회
- `edit` : 기존 영화 수정 페이지 조회
- `update` : 단일 영화 데이터 수정
- `delete` : 단일 영화 데이터 삭제



----------------------------------------------------------------------------------------------------------

#### views.py

- index

  - `order_by('-pk')` : 최신글을 위에 두기

  - 전체 영화 데이터 조회 및 index.html render

    

- new

  - 장르 데이터 제공 및 new.html 렌더링

    

- create

  - **POST 로 받은 인자값을 table에 저장**

  - 새로운 영화 데이터 저장 및 detail.html redirect

    


  - detail

    - pk(primary key) 인자를 전달 받음

    - 단일 영화 데이터 조회 및 detail.html render

      

  - edit

    - `genres` 에 선택할 영화 장르들을 전달하여 `edit.html`에서 비교할 수 있게 만들었다

    - pk(primary key) 인자를 전달 받음

    - 수정 대상 영화 데이터 조회 및 edit.html render

      

  - update

    - **request에 POST 방식으로 받은 인자값을 table에 저장(값을 변경)**

    - 영화 데이터 수정 및 detail.html redirect(pk 값 전달)

      

  - delete

    - method 가 POST 방식일때만 삭제
      - 아닐 경우 detail.html로 redirect(pk 값 전달)

    - 단일 영화 데이터 삭제 및 index.html redirect

---

#### Templates

- index.html

  - 영화 제목과 평점을 보여줌

    - **for문을 사용하여 table에 추가, 삭제, 업데이트 될때마다 반영**

    - **NEW** url

      


- new.html

  - 영화의 정보들을 받음

    

- detail.html

  - 영화의 정보들을 출력

  - `DELETE`, `EDIT`, `BACK(인덱스로 이동)` 할 수 있음

    

- edit.html

  - pk 값을 받아 선택한 영화의 정보를 그대로 받아 수정할 수 있게 함

  - Genre

    - ```django
      <div class="mb-2">
          <label for="genre" class="form-label">GENRE</label>
          <select class="form-select" name="genre" id="genre">
            {% for genre in genres %}
            {% if movie.genre == genre %}
            <option value="{{ movie.genre }}" selected>{{ genre }}</option>
            {% else %}<option value="{{ genre }}">{{ genre }}</option>
            {% endif %}
            {% endfor %}
          </select>
        </div>
      ```

      - 이전의 데이터값을 option 에 selected로 만들기 위해

        - `for문` 과  `if문`을 사용

          

  - **textarea 는 다른 input type 과 다르게 tag 사이에 value 값을 넣어야 한다!**

  - Release_date

    - ```django
      <label for="release_date">RELEASE_DATE</label>
        <input type="date" id="release_date" name="release_date" value="{{movie.release_date|date:'Y-m-d'}}">
      ```

      - `인자값|date: 'Y-m-d'` 를 통하여 날짜를 받음

        

  - `input type="reset"`

    - 모든 폼(form) 요소의 값을 초깃값으로 되돌리는 리셋 버튼(reset button)을 정의

---

## 발생한 문제

**Extension들이 겹쳐서 저장시 형식이 깨져 출력이 제대로 안되는 경우가 생겼다**

- edit.html 의 release_date을 구할때 출력이 계속 안나와서 확인해 보니 줄이 안맞았다 ㅠㅠ

- **닫는 태그가 없는 태그들에 닫는 태그가 생겼다**

  - **HTML5에서는 하나의 태그로 이루어진 것들은 닫는 태그가 없다**

    

- `views.py 의 update`

  - **CRUD 시스템을 계속 반복하며 SQL이 Django에서는 어떻게 쓰이는지 익숙해질 필요가 있다**

    

# 프로젝트 총평

- **Bootstrap 과 CSS 에 더 시간을 투자하여 능력을 키워야겠다**
- **Extension 함부로 깔지 말자**
