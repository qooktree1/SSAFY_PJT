# 관통 프로젝트 2022-04-22 [pjt08]

# 과정

### 목적

- DRF 을 활용한 API Server 제작
- Database 1:N, M:N에 대한 이해

---

## Problems

`models.py`

- Movie 클래스에 ManyToManyField 를 만들어 1:N 관계를 만드는 과정이 아직 이해가 잘 안됨

```python
# models.py
class Movie(models.Model):
    title = models.CharField(max_length=100)  # 영화제목
    overview = models.TextField()  # 줄거리
    release_date = models.DateTimeField()  # 개봉일
    poster_path = models.TextField()  # 포스터 주소

    actors = models.ManyToManyField(Actor, related_name='movies')
    

    
# serializers.py
class ActorSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = '__all__'
```

- models.py의 Movie class의 MTM 필드를 작성할때 related_name을 잘못 설정하여 serializers.py의 ActorSerializer 클래스를 작성할때 Movie 안의 값들을 받아오지 못하였음 
  - **교수님 찬스를 통해 해결완료함**!!!



`serializers.py`

- ReviewSerializer 클래스가 역참조하여 영화의 제목을 받아야하는데 못하는 중입니다.
- MovieSerializer, ActorSerializer 에서 참조 혹은 역참조로 받은 필드값 안의 필드값들의 필요하지 않은 필드를 출력하는 중입니다.



- 현재 문제점
  - serializer 와 models 사이의 field를 불러오지 못하는 문제 발생


---

# 프로젝트 총평

수정중..