
from django.db import models, IntegrityError


class Restaurant(models.Model):
    
    name = models.CharField(max_length=32 ,verbose_name='음식점 이름')
    content = models.TextField(verbose_name='음식점 설명')
    
    positive_count = models.IntegerField(default=0,verbose_name='좋아요 수')
    negative_count = models.IntegerField(default=0,verbose_name='싫어요 수')

    def __str__(self):
        return self.title
