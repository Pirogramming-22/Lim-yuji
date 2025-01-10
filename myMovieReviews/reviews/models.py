from django.db import models
from django.utils.timezone import now

class Review(models.Model):
    title = models.CharField(max_length=100)  # 영화제목
    director = models.CharField(max_length=100, default='Unknown')  # 감독
    actors = models.TextField(default='Unknown')  # 배우
    genre = models.CharField(max_length=50)  # 장르
    rating = models.FloatField()  # 별점
    running_time = models.PositiveIntegerField(null=True, blank=True)  # 러닝타임
    content = models.TextField()  # 내용
    release_year = models.PositiveIntegerField(null=True, blank=True) # 개봉연도
    updated_at = models.DateTimeField(auto_now=True)  # 수정일

    def __str__(self):
        return self.title