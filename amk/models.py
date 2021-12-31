import datetime                #

from django.db import models
from django.utils import timezone #
from django.contrib import admin
from django.urls import reverse

# Create your models here.
#데이터베이스
#-----------------------------------------------------------------------------
class Category(models.Model):
  name = models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요.(ex:일상)")

  def __str__(self):            #자기를 어떻게 표시할 것인가
    return self.name            #name으로 표시하겟다

class Post(models.Model):
  tittle = models.CharField(max_length=200)
  title_image = models.ImageField(blank=True)   # pip install Pillow   이미지필드를 사용하기위해서
  content = models.TextField()
  createDate = models.DateTimeField(auto_now_add=True)
  updateDate = models.DateTimeField(auto_now_add=True)
  #하나의 글을 여러가지의 분류에 해당될수 있다
  category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요.")

  def __str__(self):
    return self.tittle

  #1번글의 경우 -> single/1
  def get_absolute_url(self):     # 자기자신을 찾아올수있는 주소를 어떻게
    return  reverse("single", args=[str(self.id)])             #single 은 html url 이름

  def is_content_more300(self):
    return len(self.content) > 300

  def get_content_under300(self):
    return self.content[:300]

  #python manage.py makemigrations
  #python manage.py migrate
  #python manage.py createsuperuser