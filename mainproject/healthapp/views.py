from multiprocessing import context

import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.graph_objs import Figure
from django.shortcuts import render

from .forms import EntityForm
from .forms import ParticipantForm
from .models import Participant
from .forms import ContactForm
from .mllog import features
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

            Age = form.cleaned_data['age']
            BMI = form.cleaned_data['bmi']
            Sex = form.cleaned_data['sex']
            HighBP = form.cleaned_data['blood_pressure']
            PhysActivity = form.cleaned_data['physical_activity']
            MentHlth = form.cleaned_data['MentHlth']
            GenHlth = form.cleaned_data['gen_hlth']
            AnyHealthcare = form.cleaned_data['any_hlthcare']
            HvyAlcoholConsump = form.cleaned_data['Hvyalcohol']
            Veggies = form.cleaned_data['Veggies']
            Fruits = form.cleaned_data['Fruits']
            NoDocbcCost = form.cleaned_data['Nodocbccost']
            PhysHlth = form.cleaned_data['PhysHlth']
            DiffWalk = form.cleaned_data['Diffwalk']
            Smoker = form.cleaned_data['smoker']
            Stroke = form.cleaned_data['stroke']
            Income = form.cleaned_data['income']
            CholCheck = form.cleaned_data['CholCheck']
            HighChol = form.cleaned_data['HighChol']
            Education = form.cleaned_data['Education']
            HeartDiseaseorAttack = form.cleaned_data['HeartDiseaseorAttack']


            participant = Participant.objects.create(
                age = Age,
                bmi = BMI,
                blood_pressure = HighBP,
                sex = Sex,
                physical_activity = PhysActivity,
                gen_hlth = GenHlth,
                any_hlthcare = AnyHlthcare,
                Hvyalcohol = HvyAlcoholConsump,
                Veggies = Veggies,
                Fruits = Fruits,
                Nodocbccost = NoDocbcCost,
                PhysHlth = PhysHlth,
                Diffwalk = DiffWalk,
                smoker = Smoker,
                stroke = Stroke,
                income = Income,
                CholCheck = CholCheck,
                HighChol = HighChol,
                Education = Education,


            )

            input_data = [[features]]

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



