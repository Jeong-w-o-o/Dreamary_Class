from django.db import models

# Create your models here.
# 모델명의 첫 글자는 무조건 대문자
# models.py에 있는 미디아에 있는 이미지스에 올리겠다는 말.

class Designer (models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    description = models.TextField()
    
    def __str__(self):
        return self.name