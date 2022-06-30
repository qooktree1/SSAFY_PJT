# 7기 관통 프로젝트 2022-02-11 [pjt03]

# Problem!

- Navigation bar

  ```css
  nav img {
    height: 50px;
  }
  ```

  - Image의 size를 조절하는데 힘이 많이 들었다
    - 첫 접근은 width의 size를 조절해보았지만 Image 파일이 깨져 시간이 걸림
    - img 상위 태그의 문제였나 고민해보았지만 역시 해결되지 않음
    - 결과적으로 height를 바꾸었더니 원하는 결과물이 남옴
    - `Image size를 조절할 때 height를 조절하자`

  ```html
  <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <!-- ms-auto? -->
          <ul class="navbar-nav ms-auto mb-2 mb-md-0">
            <li class="nav-item">
              <a class="nav-link active" href="02_home.html">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="03_community.html">Community</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" aria-current="page" data-bs-toggle="modal" data-bs-target="#staticBackdrop" href="#">Login</a>
            </li>
          </ul>
  </div>
  ```

  - bootstrap components에서 navigation bar 폼을 가져와 사용 도중 nav-item 값들이 정렬되지 않는 문제가 발생함
    - ms-auto 왼쪽에 maring을 준다!!
    - 정확하게 개념을 알아보는 시간이 필요

- Container

  - Container를 이용해 width 값을 설정 가능한 것을 잊지 말자
  - 처음 코드를 짜느라 @media 를 통해 반응형 웹을 구성하였다
    - 여러가지 문제가 많았고 피드백을 받은 후 Container를 이용
  - Container -> div -> aside -> section 등 구조를 짜는 연습이 필요하다는 것을 느낌
  - `처음 코드를 건드릴 때 구조부터 짜는 연습을 하자`

  

# 프로젝트 총평

- **bootstrap 에서 가져와 쓰는 건 좋지만 제대로 알고 쓰자**
  - 되도록이면 내가 직접 짜서 이해를 하도록 노력해보자
  - Navbar, footer, Card 등
- `알고리즘을 공부하며 웹 공부에 소홀해진 것을 느꼈고 웹 공부도 번갈아 가며 해야 할 것 같다`

# 한 줄 결론!

`코드의 구조를 짜는 연습을 하고 제발 Container 배웠으면 써먹자!`