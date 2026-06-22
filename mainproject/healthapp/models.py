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
    
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=254)

class Participant(models.Model):
    Age = models.IntegerField(default=0)
    BMI = models.IntegerField(default=0)
    Income = models.IntegerField(default=0)
    Stroke = models.IntegerField(default=0)
    Smoker = models.IntegerField(default=0)
    CholCheck = models.IntegerField(default=0)
    Sex = models.IntegerField(default=0)
    HighBP = models.IntegerField(default=0)
    PhysActivity = models.IntegerField(default=0)
    GenHlth = models.IntegerField(default=0)
    AnyHealthcare = models.IntegerField(default=0)
    HvyAlcoholConsump = models.IntegerField(default=0)
    Veggies = models.IntegerField(default=0)
    Fruits = models.IntegerField(default=0)
    NoDocbcCost = models.IntegerField(default=0)
    PhysHlth = models.IntegerField(default=0)
    DiffWalk = models.IntegerField(default=0)
    HighChol = models.IntegerField(default=0)
    Education = models.IntegerField(default=0)
    HeartDiseaseorAttack = models.IntegerField(default=0)
    MentHlth = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Participant {self.id}'

    
class Participant2(models.Model):
    Pregnancies = models.IntegerField(default=0)
    Glucose = models.FloatField(default=0)
    BloodPressure = models.FloatField(default=0)
    SkinThickness = models.FloatField(default=0)
    Insulin = models.FloatField(default=0)
    BMI = models.FloatField(default=0.0)
    DiabetesPedigreeFunction = models.FloatField(default=0.0)
    Age = models.IntegerField(default=0)
