from multiprocessing import context

import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
from plotly.graph_objs import Figure
from django.shortcuts import render

from .forms import EntityForm
from .forms import ParticipantForm
from .models import Participant
# from .ml import logreg_cv

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
            blood_pressure = form.cleaned_data['blood_pressure']
            sex = form.cleaned_data['sex']
            physical_activity = form.cleaned_data['physical_activity']

            participant = Participant.objects.create(
                age = age,
                bmi = bmi,
                glucose = glucose,
                blood_pressure = blood_pressure,
                sex = sex,
                physical_activity = physical_activity,
            )

            input_data = [[age, bmi, glucose, blood_pressure,
                            sex, physical_activity]]

            return render(request, 'healthapp/predict.html', context)

        
        # prediction = logreg_cv.predict(input_data)[0]

        # return render(request, 'results.html',
        #               {'prediction': prediction})
    
    else:
        form = ParticipantForm()

    return render(request, 'healthapp/predict.html', {'form': form})



