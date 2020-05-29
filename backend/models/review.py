
from django.db import models, IntegrityError
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from .restaurant import Restaurant

class Review(models.Model):
    
    restaurant = models.ForeignKey(
        to=Restaurant,
        on_delete=models.CASCADE
    )
    content = models.TextField(verbose_name='리뷰 내용')
    star_rating =models.PositiveIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(5)], verbose_name='별점 (5점 만점)')
    writer = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.title
