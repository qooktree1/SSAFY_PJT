# 관통 프로젝트 2022-04-15 [pjt07]

# 과정

- 가상환경 생성
- 가상환경 활성화 후 패키지 목록 설치 with requirements.txt
- `.gitignore` 작성
- 프로젝트 생성
- 앱 생성
- urls.py
- views.py
- models.py
  - Movie
    - title
    - description
    - user_id : 외래키

  - Comment
    - content
    - movie_id
    - user_id : 외래키

- templates
- forms.py
- admin.py

### 목적

- 데이터를 생성, 조회, 수정, 삭제 가능한 웹 어플리케이션
- Django 1:N 관계에 대한 이해
- Django 인증에 대한 이해

---

## New Learned & Problems

- 댓글을 추가하고 삭제하는 기능을 만들 때 views.py 에 어떤 식으로 기본키를 가져오고 구성이 되는지 몰랐습니다.

  

- movies 에 migrations 파일 안에 테이블을 잘못 만들어 다시 삭제하는 경우가 생겨 어려웠습니다.


---

# 프로젝트 총평

- 공가로 인해 빠진 수업 및 복습을 철저히 해야 할 것 같다