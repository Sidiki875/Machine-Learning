from multiprocessing import context
import numpy as np
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.graph_objs import Figure
from django.shortcuts import render

from .forms import EntityForm
from .forms import ParticipantForm
from .models import Participant
from .forms import ContactForm
from .mllog import logreg_cv

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

            if prediction == 0:
                result = 'No diabetes'
            elif prediction == 1:
                result = 'Diabetes'
            else :
                result = 'Oops'

        # return result

            #context['result'] = result

            return render(request, 'healthapp/predict.html', {'form':ParticipantForm(), 'result':result})
    
    else:
        form = ParticipantForm()

    return render(request, 'healthapp/predict.html', {'form': form})



