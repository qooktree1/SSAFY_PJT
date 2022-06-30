# 7기 관통 프로젝트 2022-03-04 [pjt04]



# 과정

- 가상환경 생성
- 가상환경 활성화 후 패키지 목록 설치 with requirements.txt
- `.gitignore` 작성
- 프로젝트 `pjt04` 와 앱 `movies` 생성
- **프로젝트 pjt04**
  - settings.py
    - INSTALLED_APPS 안에 `movies` 추가
    - TEMPLATES 안의 DIRS 에 `[BASE_DIR / 'templates'],` 추가
      - 최상위에 templates - base.html을 쓰기 위해 추가
  - urls.py
    - `movies/` 와 `movies/recommendations` path 추가
- **최상위 폴더에 templates 추가**
  - base.html, _nav.html, _footer.html 추가
- **앱 movies**
  - views.py
    - `index 함수`와 `recommendations 함수` 추가
  - templates 폴더 추가
    - `index.html`, `recommendations.html` 추가

---

- base.html
  - templates(base, nav, footer) 를 먼저 작성 후 `상속(include)`하는 방향으로 갔다
  - _nav.html
  - _footer.html
    - 화살표 표시 font-awesome 적용
      - base.html에 `Kit's Code 추가`
      - `fa-lg` 를 이용해 크기 증가
      - size : 1.25em, 20px
      - padding값을 top에 8px 만큼 (줄 맞춤)

    - 바닥에 고정하기 위해 `fixed-bottom` 사용
    - 투명도 : `opacity-75`


----------------------------------------------------------------------------------------------------------

- movies / recommendations.html
  - **Card**
  - recommendations 함수
    - 사진과 상세정보(url)
      - `m_id : MOVIE_URL + str(영화 id)`
      - `poster_path : IMG_URL + poster_path`
    - 영화 정보들을 배열로 초기화한 후 영화 정보의 모든 정보를 append 함
    - 배열의 길이 중 한 index를 random하게 뽑은 후 content에 그 index에 해당하는 값들을 저장하는 방식을 사용
  - 처음 requests를 하는 방식이 익숙치 않아 시간을 많이 잡아 먹었다
    - 전에 했던 pjt를 참고하여 풀었다
  - 처음에는 출력해야 할 영화의 요소들을 배열로 받아 random 함수를 돌려 각기 다른 영화를 소개했다
    - 이 사실을 너무 늦게 깨달아 코드가 복잡해졌다
  - 사진을 어떻게 받아야할지 몰라 고민을 하다 팀원의 도움으로 `https://www.themoviedb.org/t/p/w500/` 뒤에 poster_path가 온다는 것을 알았다
  - 하지만, **상세정보 버튼**을 클릭하여 그 영화의 페이지로 가는 코드에 에러가 생겨 시간을 다 썼다.
    - 완료하였음

---

- movies / index.html
  - index 함수
    - 최신영화 정보 중 6개를 무작위로 골라 배열에 담아 content에 선언했다
  - **아직 모듈화는 노력중이다..**



# 프로젝트 총평

- **bootstrap grid를 다시 한번 복습하자**
- 개인 웹 프로젝트를 진행하게 되면 django에서 연습해야 할 것 같다
- **모듈화를 연습하자**
- **외부의 파일을 json형태로 받아 원하는 값을 사용하는 skill이 아직 많이 부족한것 같아 이를 숙달해야겠다**
