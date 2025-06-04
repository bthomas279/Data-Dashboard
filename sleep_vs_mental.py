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
    #Create the sleep hours bin
    df["sleep_hours_bin"] = pd.cut(
        df["sleep_hours"],
        bins = [0, 4, 6, 8, 10],
        labels = ["0-4", "4-6", "6-8", "8-10"]
    )

    #Group by the sleep hour bins and find the mental health rating mean 
    average_bin = df.groupby(['sleep_hours_bin', 'part_time_job'])['mental_health_rating'].mean().reset_index()

    #Create the interactive line plot 
    fig = px.line(
        average_bin,
        x = 'sleep_hours_bin',
        y = 'mental_health_rating',
        color = 'part_time_job',
        markers = True,
        title = "Average Mental Heath Rating vs. Sleep Hours (by Part-Time Job Status)",
        labels = {'sleep_hours_bin': 'Sleep Hours',
                  'mental_health_rating': 'Mental Health Rating'}
    )
    
    #Update fig
    fig.update_traces(line = dict(width = 3))
    fig.update_layout(yaxis_range = [0,10])


    #Creates the the visualization's own layout in the app
    v5_layout = html.Div([
            #Subtitle
            html.H2("Sleep Hours vs. Mental Health Rating"),
            html.P("""The Line Plot shows that Those with a part time job tend to have a better mental
                   health rating the more sleep hours they get after the 4 hr mark. The opposite can be said for
                   students who don't have a part time job."""),
            dcc.Graph(figure = fig)
        ])

    return v5_layout
    
