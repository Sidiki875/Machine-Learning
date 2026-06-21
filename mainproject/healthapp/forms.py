from django import forms
import pandas as pd
from django.forms import ModelForm
from .models import Participant

class EntityForm(forms.Form):
    entity = forms.CharField(max_length = 200, label='Entity/Country')

class ParticipantForm(forms.Form):
    age = forms.IntegerField(
        min_value=0,
        max_value=120,
        required = True,
        error_messages = {'required': 'Please provide your age', 'max_value': 'Please provide a realistic age'},
        label='Age'
    )
    bmi = forms.FloatField(
        min_value=0,
        max_value=100,
        label='BMI'
    )
    sex = forms.ChoiceField(
        choices=[('male','Male'), ('female', 'Female')]
    )
    blood_pressure = forms.ChoiceField(
        choices = [(0, 'Yes'),(1, 'No')],
        label=' High Blood Pressure'
    )
    physical_activity = forms.ChoiceField(
        choices= [(0, 'Yes'),(1, 'No')]
    )
    gen_hlth = forms.ChoiceField(
        choices= [(1, 'Excellent'), (2, 'Very Good'), (3, 'Good'), (4, 'Fair'), (5, 'Poor')]
    )
    any_hlthcare = forms.ChoiceField(
        choices= [(0, 'Yes'),(1, 'No')]
    )
    Hvyalcohol = forms.ChoiceField(
        choices= [(0, 'Yes'),(1, 'No')]
    )
    Veggies = forms.ChoiceField(
        choices= [(0, 'Yes'),(1, 'No')]
    )
    Fruits = forms.ChoiceField(
        choices= [(0, 'Yes'),(1, 'No')]
    )
    Nodocbccost = forms.ChoiceField(
        choices= [(0, 'Yes'),(1, 'No')]
    )
    PhysHlth = forms.IntegerField(
        min_value = 0,
        max_value = 30,
        label = 'How many days during the past 30 days was your physical health not good?'
    )
    Diffwalk = forms.ChoiceField(
        choices= [(0, 'Yes'),(1, 'No')]
    )
    smoker = forms.ChoiceField(
        choices= [(0, 'Yes'),(1, 'No')]
    )
    stroke = forms.ChoiceField(
        choices = [(0, 'Yes'),(1, 'No')]
    )
    income = forms.ChoiceField(
        choices = [(1,'Less than $10,000'),(2,'Less than $15,000'),(3,'Less than $20,000'),
                   (4,'Less than $25,000'),(5,'less than $35,000'),(6,'Less than $50,000'),(7,'Less than $75,000'),(8,'$75,000 or more')]
    )
    CholCheck = forms.ChoiceField(
        choices = [(0, 'Yes'),(1, 'No')]
    )
    HighChol = forms.ChoiceField(
        choices = [(0, 'Yes'),(1, 'No')]
    )
    Education = forms.ChoiceField(
        choices = [(1, 'Never attended school or only kindergarten'),(2, 'Grades 1 through 8 Elementary'),(3, 'Grades 9 through 11(Some high school)'),
                   (4, 'Grade 12 or GED (High School graduate)'),(5, 'College 1 year to 3 years (Some college or technical school)'),(6, 'College 4 years or more (College graduate)')]
    )
    HeartDiseaseorAttack = forms.ChoiceField(
        choices = [(0, 'Yes'),(1, 'No')]
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