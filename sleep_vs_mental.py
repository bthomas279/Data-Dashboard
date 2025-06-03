import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

#This script is for making the sleep hour svs mental health score visualization
df = pd.read_csv('database.csv')

def sleep_vs_mental():
    """Creates an interactive scatter plot based of the sleep hours per day
    and the mental health rating split by whether or not the participants have
    a part time job
    Args:
        None
    Returns:
        v5_layout: A variable which represents the visualization's layout in 
        the app.
    """
    #Interactive scatterplot set up
    fig = px.scatter(
        df, 
        x = "sleep_hours", 
        y = "mental_health_rating", 
        color = "part_time_job",
        title = "Sleep Hours vs. Mental Health Rating",
        labels = {
            "mental_health_rating": "Mental Health Rating",
            "sleep_hours": "Hours of Sleep",
            "part_time_job": "Part Time Job"},
        trendline = "ols"
    )

    #Creates the the visualization's own layout in the app
    v5_layout = html.Div([
        #Subtitle
        html.H2("Sleep Hours vs. Mental Health Score"),
        html.H3("Organized by part time job"),
        html.P(""""""), 
        dcc.Graph(figure = fig)
    ])

    return v5_layout
