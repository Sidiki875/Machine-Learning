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
    age = models.IntegerField(default=0)
    bmi = models.FloatField()
    income = models.IntegerField(default=0)
    stroke = models.IntegerField(default=0)
    smoker = models.IntegerField(default=0)
    CholCheck = models.IntegerField(default=0)
    sex = models.CharField(max_length=6, default='Male')
    blood_pressure = models.IntegerField(default=0)
    physical_activity = models.IntegerField(default=0)
    gen_hlth = models.IntegerField(default=0)
    any_hlthcare = models.IntegerField(default=0)
    Hvyalcohol = models.IntegerField(default=0)
    Veggies = models.IntegerField(default=0)
    Fruits = models.IntegerField(default=0)
    Nodocbccost = models.IntegerField(default=0)
    PhysHlth = models.IntegerField(default=0)
    Diffwalk = models.IntegerField(default=0)
    HighChol = models.IntegerField(default=0)
    Education = models.IntegerField(default=0)
    HeartDiseaseorAttack = models.IntegerField(default=0)
    MentHlth = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Participant {self.id}'

    

