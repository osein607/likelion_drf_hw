from django.db import models

# Create your models here.
# 좋아하는 가수(Singer) 모델과 유명한 노래(Song) 모델을 이용한 가수 설명서를 작성해주세요. 
# - Singer 모델에는 id, content(가수설명), debut(데뷔일자)가 필수로 있어야 합니다.
# - Song 모델에는 id, singer(해당 노래 부른 사람, ForeignKey), release(출시일), content(노래 설명)이 필수로 있어야 합니다

class Singer(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=50)
  content = models.TextField()
  debut = models.DateTimeField()

class Song(models.Model):
  id = models.AutoField(primary_key=True)
  singer = models.ForeignKey(Singer, blank=False, null=False, on_delete=models.CASCADE, related_name='songs')
  name = models.CharField(max_length=50, blank=True, null=True)
  release = models.DateTimeField()
  content = models.TextField()