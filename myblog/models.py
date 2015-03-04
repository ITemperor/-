from django.db import models

class myblog(models.Model):
	biaoti=models.CharField(max_length=30)
	neirong=models.TextField(max_length=1024)
	img=models.ImageField(upload_to = './img')
