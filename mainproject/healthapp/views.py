from multiprocessing import context

import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.graph_objs import Figure
from django.shortcuts import render

from .forms import EntityForm
from .forms import ParticipantForm
from .models import Participant
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

def predict(request):

    if request.method == 'POST':

        form = ParticipantForm(request.POST)

        context['form'] = ParticipantForm()

        if form.is_valid():

            age = form.cleaned_data['age']
            bmi = form.cleaned_data['bmi']
            glucose = form.cleaned_data['glucose']
            sex = form.cleaned_data['sex']
            blood_pressure = form.cleaned_data['blood_pressure']
            physical_activity = form.cleaned_data['physical_activity']
            gen_hlth = form.cleaned_data['gen_hlth']
            any_hlthcare = form.cleaned_data['any_hlthcare']
            Hvyalcohol = form.cleaned_data['Hvyalcohol']
            Veggies = form.cleaned_data['Veggies']
            Fruits = form.cleaned_data['Fruits']
            Nodocbccost = form.cleaned_data['Nodocbccost']
            PhysHlth = form.cleaned_data['PhysHlth']
            Diffwalk = form.cleaned_data['Diffwalk']
            smoker = form.cleaned_data['smoker']
            stroke = form.cleaned_data['stroke']
            income = form.cleaned_data['income']
            CholCheck = form.cleaned_data['CholCheck']
            HighChol = form.cleaned_data['HighChol']
            Education = form.cleaned_data['Education']

            participant = Participant.objects.create(
                age = age,
                bmi = bmi,
                glucose = glucose,
                blood_pressure = blood_pressure,
                sex = sex,
                physical_activity = physical_activity,
                gen_hlth = gen_hlth,
                any_hlthcare = any_hlthcare,
                Hvyalcohol = Hvyalcohol,
                Veggies = Veggies,
                Fruits = Fruits,
                Nodocbccost = Nodocbccost,
                PhysHlth = PhysHlth,
                Diffwalk = Diffwalk,
                smoker = smoker,
                stroke = stroke,
                income = income,
                CholCheck = CholCheck,
                HighChol = HighChol,
                Education = Education,


            )

            input_data = [[age, bmi, blood_pressure,
                            sex, physical_activity, gen_hlth,
                              any_hlthcare, Hvyalcohol, Veggies,
                                Fruits, Nodocbccost, PhysHlth,
                                  Diffwalk, smoker, stroke,
                                    income, CholCheck, HighChol, Education]]

            return render(request, 'healthapp/predict.html', context)

        
        prediction = logreg_cv.predict(input_data)[0]

        if prediction == 0:
            result = 'No diabetes'
        elif prediction == 1:
            result = 'Diabetes'
        else :
            result = 'Oops'

        # return result

        return render(request, 'healthapp/predict.html',
                      {'result': result})
    
    else:
        form = ParticipantForm()

    return render(request, 'healthapp/predict.html', {'form': form})



