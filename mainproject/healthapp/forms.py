from django import forms
import pandas as pd
from django.forms import ModelForm
from .models import Participant

class EntityForm(forms.Form):
    entity = forms.CharField(max_length = 200, label='Entity/Country')

class ContactForm(forms.Form):
    name = forms.CharField(max_length= 100)
    message = forms.CharField(widget=forms.Textarea)

class ParticipantForm(forms.Form):
    Age = forms.IntegerField(
        min_value=0,
        max_value=120,
        required = True,
        error_messages = {'required': 'Please provide your age', 'max_value': 'Please provide a realistic age'},
        label='Age'
    )
    BMI = forms.IntegerField(
        min_value=0,
        max_value=100,
        label='BMI'
    )
    Sex = forms.TypedChoiceField(
        choices = [('', 'Select Gender'),(0,'Female'), (1, 'Male')],
        coerce = int,
    )
    HighBP = forms.TypedChoiceField(
        choices = [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label=' High Blood Pressure'
    )
    PhysActivity = forms.TypedChoiceField(
        choices= [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Physical activity in the past 30 days, not including job?'
    )
    GenHlth = forms.TypedChoiceField(
        choices= [('', 'Select'),(1, 'Excellent'), (2, 'Very Good'), (3, 'Good'), (4, 'Fair'), (5, 'Poor')],
        coerce = int,
        label = 'Would you say that in general your health is?'
    )
    AnyHealthcare = forms.TypedChoiceField(
        choices= [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Have any kind of health care coverage, including health insurance, prepaid plans such as HMO, etc.?'
    )
    HvyAlcoholConsump = forms.TypedChoiceField(
        choices= [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)?'
    )
    Veggies = forms.TypedChoiceField(
        choices= [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Consume Vegetables 1 or more times per day ?'
    )
    Fruits = forms.TypedChoiceField(
        choices= [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Consume Fruit 1 or more times per day ?'
    )
    NoDocbcCost = forms.TypedChoiceField(
        choices= [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?'
    )
    PhysHlth = forms.IntegerField(
        min_value = 0,
        max_value = 30,
        label = 'How many days during the past 30 days was your physical health not good?'
    )
    DiffWalk = forms.TypedChoiceField(
        choices= [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Do you have serious difficulty walking or climbing stairs?'
    )
    Smoker = forms.TypedChoiceField(
        choices= [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Have you smoked at least 100 cigarettes in your entire life ?'
    )
    Stroke = forms.TypedChoiceField(
        choices = [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = '(Ever told) you had a stroke?'
    )
    Income = forms.TypedChoiceField(
        choices = [('', 'Select'),(1,'Less than $10,000'),(2,'Less than $15,000'),(3,'Less than $20,000'),
                   (4,'Less than $25,000'),(5,'less than $35,000'),(6,'Less than $50,000'),
                   (7,'Less than $75,000'),(8,'$75,000 or more')],
        coerce = int,
        label = 'What is your annual income?'
    )
    CholCheck = forms.TypedChoiceField(
        choices = [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Has your cholesterol been checked in the past 5 years ?'
    )
    HighChol = forms.TypedChoiceField(
        choices = [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Is your Cholesterol high ?'
    )
    Education = forms.TypedChoiceField(
        choices = [('', 'Select'),(1, 'Never attended school or only kindergarten'),(2, 'Grades 1 through 8 Elementary'),(3, 'Grades 9 through 11(Some high school)'),
                   (4, 'Grade 12 or GED (High School graduate)'),(5, 'College 1 year to 3 years (Some college or technical school)'),
                   (6, 'College 4 years or more (College graduate)')],
        coerce = int,
        label = 'What is your highest level of education ?'
    )
    HeartDiseaseorAttack = forms.TypedChoiceField(
        choices = [('', 'Select'),(0, 'Yes'),(1, 'No')],
        coerce = int,
        label = 'Do you have a history of Coronary heart disease (CHD) or Myocardial infarction (MI) ?'
    )
    MentHlth = forms.IntegerField(
        min_value = 0,
        max_value = 30,
        label = '	Now thinking about your mental health, which includes stress, depression, and problems with emotions, for how many days during the past 30 days was your mental health not good?'
    )


# class ParticipantForm(ModelForm):
#     class Meta:
#         model = Participant
#         fields = ['age', 'bmi', 'glucose', 'blood_pressure','gender']

class Participant2Form(forms.Form):
    Pregnancies = forms.IntegerField(
        min_value = 0,
        max_value = 30,
        label = 'Number of times pregnant'
    )
    Glucose = forms.FloatField(
        min_value = 45,
        max_value = 200,
        label = 'Plasma glucose concentration a 2 hours in an oral glucose tolerance test'
    )
    BloodPressure = forms.FloatField(
        min_value = 20,
        max_value = 180,
        label = 'Diastolic blood pressure (mm Hg)'
    )
    SkinThickness = forms.FloatField(
        min_value = 7,
        max_value = 79,
        label = 'Triceps skin fold thickness (mm)'
    )
    Insulin = forms.FloatField(
        min_value = 13,
        max_value = 859,
        label = '2-Hour serum insulin (muU/ml)'
    )
    BMI = forms.FloatField(
        min_value = 13,
        max_value = 80,
        label = 'Body mass index (BMI)'
    )
    DiabetesPedigreeFunction = forms.FloatField(
        min_value = 0.078,
        max_value = 3,
        label = 'Diabetes pedigree function'
    )
    Age = forms.IntegerField(
        min_value = 0,
        max_value = 120,
        label = 'Age'
    )