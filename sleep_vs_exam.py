from dash import dcc, html
import plotly.express as px
import pandas as pd

#This script is for making the sleep hours vs exam scores visualization
df = pd.read_csv('database.csv')

def sleep_exam_contour():
    """Creates a contour plot visualizing the sleep hours and exam scores to
    spot data clusters in the space.
    Args:
        None.
    Returns:
        v7_layout: A variable which represents the visualization's layout in 
        the app.
    """
    #Create the contour plot
    fig = px.density_contour(
        df,
        x = "sleep_hours",
        y = "exam_score",
        marginal_x = "histogram",
        marginal_y = "histogram",
        title = "Sleep Hours vs. Exam Scores Contour Plot",
        labels = {
            "sleep_hours": "Sleep Hours",
            "exam_score": "Exam Scores"
        }
    )


    #Creates the the visualization's own layout in the app
    v7_layout = html.Div([
            #Subtitle
            html.H2("Sleep Hours vs. Exam Scores"),
            html.P(""""""),
            dcc.Graph(figure = fig)
        ])

    return v7_layout
    
