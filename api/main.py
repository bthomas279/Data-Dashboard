#This script puts the other scripts together into one
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import flask
import pandas as pd
from dash import html
from exam_scores import exam_scores
from media_vs_sleep import media_vs_sleep
from study_vs_media import gender_work_social
from mental_vs_exam import mental_vs_exam
from sleep_vs_mental import sleep_vs_mental
from diet_vs_mental import mental_diet_violin
from sleep_vs_exam import sleep_exam_contour

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
df = pd.read_csv('database.csv')

#Create the final layout
app.layout = html.Div([
    html.H1("Dash App Dashboard"),
    html.Hr(),
    exam_scores(),
    html.Hr(),
    media_vs_sleep(),
    html.Hr(),
    gender_work_social(),
    html.Hr(),
    mental_vs_exam(),
    html.Hr(),
    sleep_vs_mental(),
    html.Hr(),
    mental_diet_violin(),
    html.Hr(),
    sleep_exam_contour()
])

app = server

def handler(environ, start_response):
    return server(environ, start_response)