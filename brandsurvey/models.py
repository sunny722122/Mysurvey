from django.db import models
from django.forms import ModelForm

# Create your models here.
class Question(models.Model):
    ques=models.CharField(max_length=100)
    def __str__(self):
        return self.ques

class Option(models.Model):
    option=models.CharField(max_length=100)
    check=models.BooleanField()
    def __str__(self):
        return f"{self.option}:{self.check}"

class Result(models.Model):
    
    result=models.CharField(max_length=1000)
    def __str__(self):
        return self.result
   
""" class Survey(models.Model):
    question=models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="question"
    )
    option=models.ForeignKey(Option,on_delete=models.CASCADE)
     """
""" class SurveyForm(ModelForm):
    class Meta:
        model=  Survey
        fields=('question','choices')   """