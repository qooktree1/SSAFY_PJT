from django.db import models
from django.conf import settings


class Movie(models.Model):
    title = models.CharField(max_length=20)  # 영화 제목
    description = models.TextField()  # 줄거리
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)



class Comment(models.Model):
    content = models.CharField(max_length=100)  # 영화 제목
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.content