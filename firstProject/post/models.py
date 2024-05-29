from django.db import models

# Create your models here.
class Post(models.Model):
    username=models.CharField(max_length=20)
    description=models.TextField()
    comment=models.CharField(max_length=30,default="this is comment")

#Create class name student 
class Student(models.Model):
    name=models.CharField(max_length=50)  
    classname=models.CharField(max_length=20)

    def __str__(self):
        return self.name


