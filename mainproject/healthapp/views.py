from multiprocessing import context
import numpy as np
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.graph_objs import Figure
from django.shortcuts import render

from .forms import EntityForm
from .forms import ParticipantForm
from .forms import Participant2Form
from .forms import Participant3Form
from .forms import ContactForm

from .models import Participant
from .models import Participant2
from .models import Participant3

from .mllog import logreg_cv
from .ml2log import logistreg_cv

# Create your views here.

def index(request):

    if request.method == 'GET':

        entity = request.GET.get('entity')

        from .dashbo import line_graph

        lineplot = line_graph()

        line_graph_div : str = plot(lineplot, output_type='div')

        if request.GET:
            lineplot = line_graph(a=entity)
            line_graph_div : str = plot(lineplot, output_type='div')
            context: dict = {'title': 'Diabetes'+' in '+ str(entity), 'lineplot': line_graph_div}
        else:
            context: dict = {'title': 'Diabetes in The UK', 'lineplot': line_graph_div}
        context['country'] = EntityForm()


    return render(request, 'healthapp/base.html', context)

def contact_view(request):
    result= None

    if request.method == "POST":
        contacts = ContactForm(request.POST)
        if contacts.is_valid():
            name = contacts.cleaned_data["name"]
            message = contacts.cleaned_data["message"]

            result = f"Thanks {name}, we received: {message}"
    else:
        contacts = ContactForm()

    return render(request, 'healthapp/contact.html', {'contacts': contacts, 'result': result})

def predict(request):

    result = None

    if request.method == 'POST':

        form = ParticipantForm(request.POST)

        #context['form'] = ParticipantForm(request.POST)

        if form.is_valid():

            Age = form.cleaned_data['Age']
            BMI = form.cleaned_data['BMI']
            Sex = form.cleaned_data['Sex']
            HighBP = form.cleaned_data['HighBP']
            PhysActivity = form.cleaned_data['PhysActivity']
            MentHlth = form.cleaned_data['MentHlth']
            GenHlth = form.cleaned_data['GenHlth']
            AnyHealthcare = form.cleaned_data['AnyHealthcare']
            HvyAlcoholConsump = form.cleaned_data['HvyAlcoholConsump']
            Veggies = form.cleaned_data['Veggies']
            Fruits = form.cleaned_data['Fruits']
            NoDocbcCost = form.cleaned_data['NoDocbcCost']
            PhysHlth = form.cleaned_data['PhysHlth']
            DiffWalk = form.cleaned_data['DiffWalk']
            Smoker = form.cleaned_data['Smoker']
            Stroke = form.cleaned_data['Stroke']
            Income = form.cleaned_data['Income']
            CholCheck = form.cleaned_data['CholCheck']
            HighChol = form.cleaned_data['HighChol']
            Education = form.cleaned_data['Education']
            HeartDiseaseorAttack = form.cleaned_data['HeartDiseaseorAttack']


            participant = Participant.objects.create(
                Age = Age,
                BMI = BMI,
                HighBP = HighBP,
                Sex = Sex,
                PhysActivity = PhysActivity,
                GenHlth = GenHlth,
                AnyHealthcare = AnyHealthcare,
                HvyAlcoholConsump = HvyAlcoholConsump,
                Veggies = Veggies,
                Fruits = Fruits,
                NoDocbcCost = NoDocbcCost,
                PhysHlth = PhysHlth,
                DiffWalk = DiffWalk,
                Smoker = Smoker,
                Stroke = Stroke,
                Income = Income,
                CholCheck = CholCheck,
                HighChol = HighChol,
                Education = Education,
                HeartDiseaseorAttack = HeartDiseaseorAttack,
                MentHlth = MentHlth,


            )

            input_data = [HighBP, HighChol, CholCheck, BMI,
                            Smoker, Stroke, HeartDiseaseorAttack, PhysActivity,
                            Fruits, Veggies, HvyAlcoholConsump,
                            AnyHealthcare, NoDocbcCost, GenHlth,
                            MentHlth, PhysHlth, DiffWalk,
                            Sex, Age, Education, Income
                        ]
            
            input_data = np.array(input_data).reshape(1, -1)

            # return render(request, 'healthapp/predict.html', context)

        
            prediction = logreg_cv.predict(input_data)[0]
            prediction_proba = logreg_cv.predict_proba(input_data)[0]
            

            if prediction == 0:
                result = 'No diabetes'
                result_proba = f'{prediction_proba[0]:.2f}'
            elif prediction == 1:
                result = 'Diabetes'
                result_proba = f'{prediction_proba[1]:.2f}'
            else :
                result = 'Oops'
                result_proba = None
                

        # return result

            #context['result'] = result

            return render(request, 'healthapp/predict.html', {'form':form, 'result':result, 'result_proba':result_proba})
    
    else:
        form = ParticipantForm()

    return render(request, 'healthapp/predict.html', {'form': form})


def predict2(request):

    result = None

    if request.method == 'POST':

        form2 = Participant2Form(request.POST)

        if form2.is_valid():

            Pregnancies = form2.cleaned_data['Pregnancies']
            Glucose = form2.cleaned_data['Glucose']
            BloodPressure = form2.cleaned_data['BloodPressure']
            SkinThickness = form2.cleaned_data['SkinThickness']
            Insulin = form2.cleaned_data['Insulin']
            BMI = form2.cleaned_data['BMI']
            DiabetesPedigreeFunction = form2.cleaned_data['DiabetesPedigreeFunction']
            Age = form2.cleaned_data['Age']

            participant2 = Participant2.objects.create(
                Pregnancies = Pregnancies,
                Glucose = Glucose,
                BloodPressure = BloodPressure,
                SkinThickness = SkinThickness,
                Insulin = Insulin,
                BMI = BMI,
                DiabetesPedigreeFunction = DiabetesPedigreeFunction,
                Age = Age,
            )

            input_data = [Pregnancies, Glucose, BloodPressure, 
                          SkinThickness, Insulin, BMI,
                           DiabetesPedigreeFunction, Age]
            
            input_data = np.array(input_data).reshape(1, -1)

            prediction2 = logistreg_cv.predict(input_data)[0]

            prediction2_proba = logistreg_cv.predict_proba(input_data)[0]

            if prediction2 == 0:
                result = 'No diabetes'
                result_proba = f'{prediction2_proba[0]:.2f}'
            elif prediction2 == 1:
                result = 'Diabetes'
                result_proba = f'{prediction2_proba[1]:.2f}'
            else:
                result = 'Oops'
                result_proba = 'Not Available'


            return render(request, 'healthapp/predict2.html', {'form2':form2, 'result':result, 'result_proba':result_proba})
        
    else:
        form2 = Participant2Form()

    return render(request, 'healthapp/predict2.html', {'form2': form2})

def survey(request):

    result = None

    if request.method == 'POST':

        form3 = Participant3Form(request.POST)

        if form3.is_valid():

            Sex = form3.cleaned_data['Sex']
            Age = form3.cleaned_data['Age']
            Height = form3.cleaned_data['Height']
            Weight = form3.cleaned_data['weight']
            BMI = form3.cleaned_data['BMI']
            Smoking = form3.cleaned_data['Smoking']
            Alcohol = form3.cleaned_data['Alcohol']
            Duration = form3.cleaned_data['Duration']
            DMac = form3.cleaned_data['DMac']
            DMic = form3.cleaned_data['DMic']
            Comorbidities = form3.cleaned_data['Comorbidities']
            HypoglycemicAgent = form3.cleaned_data['HypoglycemicAgent']
            FPGlucose = form3.cleaned_data['FPGlucose']
            PPGlucose = form3.cleaned_data['PPGlucose']
            FCpeptide = form3.cleaned_data['FCpeptide']
            Ppeptide = form3.cleaned_data['Ppeptide']
            Fastinsulin = form3.cleaned_data['Fastinsulin']
            Postinsulin = form3.cleaned_data['Postinsulin']
            HbA1c = form3.cleaned_data['HbA1c']
            GAlbumin = form3.cleaned_data['GAlbumin']
            TCholesterol = form3.cleaned_data['TCholesterol']
            Triglyceride = form3.cleaned_data['Triglyceride']
            HDLC = form3.cleaned_data['HDLC']
            LDLC = form3.cleaned_data['LDLC']
            Creatinine = form3.cleaned_data['Creatinine']
            EGFR = form3.cleaned_data['EGFR']
            UAcid = form3.cleaned_data['UAcid']
            BUN = form3.cleaned_data['BUN']
            Hypoglycemia = form3.cleaned_data['Hypoglycemia']

        
        participant3 = Participant3.objects.create(
            Sex = Sex,
            Age = Age,
            Height = Height,
            Weight = Weight,
            BMI = BMI,
            Smoking = Smoking,
            Alcohol = Alcohol,
            Duration = Duration,
            DMac = DMac,
            DMic = DMic,
            Comorbidities = Comorbidities,
            HypoglycemicAgent = HypoglycemicAgent,
            FPGlucose = FPGlucose,
            PPGlucose = PPGlucose,
            FCpeptide = FCpeptide,
            Ppeptide = Ppeptide,
            Fastinsulin = Fastinsulin,
            Postinsulin = Postinsulin,
            HbA1c = HbA1c,
            GAlbumin = GAlbumin,
            TCholesterol = TCholesterol,
            Triglyceride = Triglyceride,
            HDLC = HDLC,
            LDLC = LDLC,
            Creatinine = Creatinine,
            EGFR = EGFR,
            UAcid = UAcid,
            BUN = BUN,
            Hypoglycemia = Hypoglycemia,
        )

