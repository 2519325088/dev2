from django.db import models


# Create your models here.

class World(models.Model):
    wname=models.CharField(max_length=20)
    wtime=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.wname

class State(models.Model):
    sname=models.CharField(max_length=30)
    sgender=models.CharField(max_length=20)
    worldid=models.ForeignKey('World',on_delete=models.CASCADE)

    def __str__(self):
        return self.sname