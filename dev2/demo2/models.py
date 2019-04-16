from django.db import models

# Create your models here.

class World(models.Model):
    wname=models.CharField(max_lenth=20)
    wtime=models.DateTimeField(auto_now_add=True)

class State(models.Model):
    sname=models.CharField(max_length=30)
    sgender=models.CharField(max_length=20)
    worldid=models.ForeignKey('World',on_delete=models.CASCADE)