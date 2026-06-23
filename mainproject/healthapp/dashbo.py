import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc


def line_graph(a='United Kingdom'):

    df = pd.read_csv("https://ourworldindata.org/grapher/death-rate-from-diabetes-ghe.csv?v=1&csvType=full&useColumnShortNames=false", storage_options = {'User-Agent': 'Our World In Data data fetch/1.0'})

    def update_graph(value):
        dff = df[df.Entity==value]
        #color_map = {'Death rate from diabetes mellitus among both sexes':'darkred'}
        dff_line = px.line(dff, x='Year', y='Death rate from diabetes mellitus among both sexes', template= 'plotly_white')
        dff_line.update_traces(line_color='red')
        dff_line.update_layout(plot_bgcolor='whitesmoke')
        return dff_line

    return update_graph(str(a))


