# pjt10

## 💁🏼‍♂️구현 시 어려운 점 & 헷갈린 부분

### MovieCard.vue + HomeView.vue

- 카드 하나하나 정보를 받아와서 home에서 보여주어야 할 때, TMDB로 api key를 활용하여 정보를 받아서 보여주어야하는 과정에서 도대체 어디서 어떻게 주고 받아와야 하는지 헷갈렸다.
- Vuex를 활용하기 떄문에 state에 정보를 받아와서 card로 뿌려주는 방식으로 card를 완성하는 것이라 생각하여 api를 Vuex에서 작성하려고 했다. 하지만 실패
- 결국 HomeView 에서 axios로 정보를 받은 후 Card로 상속을 주었다.
- Card로 상속을 주는 과정에서 이미지를 받는게 또 문제가 생겼다. 그래서 이미지 path정보를 data로 만들어서 this.card.poster_path 정보를 이미지 URL에 더해서 출력할 수 있도록 했다.

- 카드를 리스트로 받아서 돌리면서 화면에 보여주는데, 부트스트랩으로 크기를 조절하는 과정에서 다사다난한 과정을 겪었다.



### RandomView.vue

- 정보를 다시 axios 입력해서 사용하기에는 너무 반복 작업이라서 emit과 props 과정을 거치려고 했으나 실패..?
- 자꾸 PointerEvent 값을 받아오는 RandomPick..
- console에서 random 페이지만 404 not found를 발생시켰다. 하지만 주소가 잘못된 것이라 생각하고 디버깅을 해도 찾을 수 없었다. (에러가 아예 안뜸...)
  - random#:1          GET http://localhost:8080/random 404 (Not Found)
- 알고보니 카드 내에 있는 img src 부분이 문제였고, 그것이 404를 불러오는 것이었다. 이후에 차근차근 처음부터 지워나가면서 정보를 어디서 못보내고 있는지 디버깅을 진행했다..
- HomeView에서 Vuex로 정보를 보낼 때 빈 배열을 보내고 있었고 수정을 하여 제대로 정보를 보낼 수 있도록 변경하였다.
- 이차원 배열로 들어가게 되면서 이 배열을 풀어서 정보를 가져오는 방식을 찾는다.
- 최종적으로 받을 때 null로 받으면 안되었었다.



### App.vue

- HomeView에 있던 axios를 App에 이전함
- 그리고 App에서 정보를 Vuex로 전송하고 그 정보를 받아서 HomeView와 RandomView에서 사용할 수 있도록 했다.

- Homeview는 정상적으로 작동하나, RandomView에서 pick을 눌렀을 때 문제가 발생, 제대로 파일이 뽑히지 않았다. 그리고 이미지 파일 변수를 data로 정의한 후에 출력을 시도했으나 아예 카드가 사라지게 되었다.




## 😭협업 시 어려웠던 부분

- 최강 협업...! 대면으로 협업하면 더욱 환상일 것 같습니다.



## 👩🏼‍💻앞으로 공부해야 할 부분👨🏼‍💻

- 전체적인 Vue, Vuex 구문
- Django
