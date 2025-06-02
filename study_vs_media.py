import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

#This script is for making the study hours vs social media hours visualization
#May use males and females variation depending on the visuals
df = pd.read_csv('database.csv')

def gender_work_social():
    """Creates a grouped bar chart that graphs the work hours and the social media
    hours for each gender.
    Args:
        None
    Returns:
        v3_layout = A variable which represents the gender_work_social method's
        layout in the app.
    """
    #Finding the average hours of the study hours and social media hours column
    mean_hours = df.groupby('gender', observed = True)[['study_hours_per_day', 'social_media_hours']].mean().reset_index()
    
    #Creating the lotting categories using .melt
    datamelt = mean_hours.melt(id_vars = "gender", var_name = "Screen Use", value_name = "hours")

    #Put togther the grouoed bar chart constraints
    fig = px.bar(
        datamelt,
        x = "gender",
        y = "hours",
        color = "Screen Use",
        barmode = 'group',
        title = 'Average Study vs. Social Media Hours by Gender',
        labels = {'gender': "Gender", 'hours': 'Average Hours'}
    )

    #Creates the the visualization's own layout in the app
    v3_layout = html.Div([
        #Subtitle
        html.H2("Study Hours vs Social Media Hours in Gender"),
        html.P("""The grouped bar plot shows that there is not a big difference between the amount of study and social media hours 
               for each gender. Average study and social media hours have about the same ratio."""), 
        dcc.Graph(figure = fig)
    ])

    return v3_layout 

