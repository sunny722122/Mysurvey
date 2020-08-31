from django.db import models

# Create your models here.
class Question(models.Model):
    question=models.CharField(max_length=100)
    def __str__(self):
        return self.question

class Option(models.Model):
    option=models.CharField(max_length=100)
    check=models.BooleanField()
    def __str__(self):
        return f"{self.option}:{self.check}"

class Result(models.Model):
    result=models.CharField(max_length=1000)
    def __str__(self):
        return self.result
    
    
    