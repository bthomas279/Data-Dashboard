from dash import html, dcc
import pandas as pd
import plotly.express as px

df = pd.read_csv('database.csv')

def exam_scores():
    """The exam_scores_hist method creates a histogram that shows
    the variation of the scores in the database. 
    Args:
        None
    Returns:
        v1_layout: A variable which represents the exam_scores method's
        layout in the app
    """
    fig = px.histogram(df, x = "exam_score", title = "Exam Score Distribution")

    v1_layout = html.Div([
        #Subtitle
        html.H2("Exam Score Distribution"),
        dcc.Graph(figure = fig)
    ])
    return v1_layout