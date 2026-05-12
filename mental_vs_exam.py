from dash import dcc, html
import plotly.express as px
import pandas as pd

#This script is for making the social media hours vs sleep visualization
df = pd.read_csv('database.csv')

def mental_vs_exam():
    """Creates a Density Heatmap that visualizes mental health scores vs the
    exam scores.
    Args:
        None 
    Returns:
        v4_layout:A variable which represents the mental_vs_exam method's
        layout in the app.
    """
    #Put the exam scores into ranges
    df['exam_score_bin'] = pd.cut(
        df['exam_score'],
        bins = [0.0, 50.0, 60.0, 70.0, 80.0, 90.0, 100.0],
        labels = ["0.0-50.0", "50.0-60.0", "60.0-70.0", "70.0-80.0", "80.0-90,0", "90.0-100.0"]
    )    

    #Combine the mental health rating and exam score bins
    heatingmap = df.groupby(['mental_health_rating', 'exam_score_bin'], observed = True).size().reset_index(name = 'count')

    #Create the visualization for dash
    fig = px.density_heatmap(
        heatingmap,
        x = 'mental_health_rating',
        y = 'exam_score_bin',
        z = 'count',
        color_continuous_scale = 'Viridis',
        title = 'Exam Scores by Mental Health Rating Heatmap',
        labels = {
            'mental_health_rating': "Mental Health Rating",
            'exam_score_bin': 'Exam Score Range',
            'count': 'Number of Students'
        }
    )

    #Creates the the visualization's own layout in the app
    v4_layout = html.Div([
        #Subtitle
        html.H2("Mental Health Rating vs. Exam Scores"),
        html.P("""Based on the heatmap shown, not many students had a mental health rating
               above 10 and the exam score distribution is almost flat. The majority of students with a mental 
               health rating between 5 and 10 tended to recive an exam score between 60 and 100. Finally,
               studnets with a 0-5 mental health rating tended to perform worse than those with a rating of
               5-10, with most students only scoring between a 0 and 80."""), 
        dcc.Graph(figure = fig)
    ])

    return v4_layout