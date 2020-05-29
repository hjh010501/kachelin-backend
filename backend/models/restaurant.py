
from django.db import models, IntegrityError
from django.contrib.auth.models import User

class Restaurant(models.Model):
    
    name = models.CharField(max_length=32 ,verbose_name='음식점 이름')
    content = models.TextField(verbose_name='음식점 설명')
    location = models.TextField(verbose_name='음식점 위치')
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
