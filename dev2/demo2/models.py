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

    def skill(self):
        return self.sgender

    skill.short_description='位置'



class Shouji(models.Model):
    name=models.CharField(max_length=30)


class yingyong(models.Model):
    yname=models.CharField(max_length=30)

    yshouji=models.ManyToManyField(to='Shouji')


#第二种：
class StudentManage(models.Manager):
    def create_book(self,_name,_age):
        # 内部使用self.mode()获取模型
        s1=self.model()
        s1.sname=_name
        s1.age=_age
        s1.save()
# 第三种：可以在管理类中调用self.create 可以不使用save()
class studentmanage1(models.Manager):
    def create_book(self,_name,_age):
        s1=self.create(sname=_name,age=_age)
        return s1

class Student(models.Model):
    sname=models.CharField(max_length=30)
    age=models.IntegerField()

# 创建对象
    # 第二种：自定义管离器
    stmage=StudentManage()

# 创建对象
    #第三种：
    stmage1=studentmanage1()



# 元选项  在模型中定义类Mate，用于设置元信息
    class Meta():
        # db_table：定义数据表名称
        db_table = 'student'
        #ordering 对象的排序字段，获取对象的列表时使用，接收属性构成的列表
        #字符串前加 — 表示倒序  不加 - 表示正序
        ordering = ['age','-sname']   #排序会增加数据库的开销H

# 创建对象
    # 第一种：在模型类中添加一个类方法
    @classmethod
    def creat(cls,_name,_age):
        student=cls(sname=_name,age=_age)
        return student