import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)

class Participant(models.Model):
    age = models.IntegerField(max_length=3)
    bmi = models.FloatField()
    income = models.IntegerField()
    stroke = models.IntegerField()
    smoker = models.IntegerField()
    CholCheck = models.IntegerField()
    sex = models.CharField(max_length=6)
    blood_pressure = models.IntegerField()
    glucose = models.IntegerField()
    physical_activity = models.IntegerField()
    gen_hlth = models.IntegerField()
    any_hlthcare = models.IntegerField()
    Hvyalcohol = models.IntegerField()
    Veggies = models.IntegerField()
    Fruits = models.IntegerField()
    Nodocbccost = models.IntegerField()
    PhysHlth = models.IntegerField()
    Diffwalk = models.IntegerField()
    HighChol = models.IntegerField()
    Education = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Participant {self.id}'

    

