from dash import html, dcc
import plotly.express as px
import pandas as pd

#This script is for making the social media hours vs sleep visualization
df = pd.read_csv('database.csv')

def media_vs_sleep():
    """Creates a boxplot for the social media hours vs sleep hours
    visualization
    Args:
        None
    Returns:
        v2_layout: A variable which represents the visualization's 
        layout in the app
    
    """
    #Create the bins and labels for the boxplot to split up the data
    df['social_media_group'] = pd.cut(
        df['social_media_hours'],
        bins = [0, 2, 3, 4, 6, 8, 10],
        labels = ["0-2", "2-4", "4-6", "6-8", "8-10", "10+"]
    )

    #Ploty doesn't have the capability of finding the mean
    #To solve this, I'm going add the mean to each row as hover data using groupby and transform
    group_means = df.groupby('social_media_group', observed = True)['sleep_hours'].transform('mean')
    df['mean_sleep_hours'] = group_means

    #Create the boxplot
    fig = px.box(
        df,
        x = "social_media_group",
        y = "sleep_hours",
        points = "all",
        hover_data = ['mean_sleep_hours'],
        color = "social_media_group",
        title = "Sleep Hours VS Social Media Usage",
        labels = {"social_media_group": "Social Media Hours",
                  "sleep_hours": "Sleep Hours"}
    )
    
    #Creates the the visualization's own layout in the app
    v2_layout = html.Div([
        html.H2("Social Media Hours VS Sleep Hours"),
        html.P("""This Boxplot shows that there is a small difference between the mean
        sleep hours and the social media hours ranges. However this does not apply to the social media 
        hour range of 8-10, who has a much lower average sleep amount."""),
        dcc.Graph(figure = fig)
    ])

    return v2_layout