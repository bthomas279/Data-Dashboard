from dash import html, dcc
import plotly.express as px
import pandas as pd

#This script is for making the diet quality vs mental heath rating visualization
df = pd.read_csv('database.csv')

def mental_diet_violin():
    """A Violin PLot that visualizes the diet quality vs the mental health
    rating. 
    Args:
    
    Returns:
        v6_layout: A variable which represents the method's visualization 
        layout in the app
    """
    violin_means = df.groupby('diet_quality', observed = True)['mental_health_rating'].transform('mean')
    df["mean_mental_health"] = violin_means

    fig = px.violin(
        df,
        x = "diet_quality",
        y = "mental_health_rating",
        box = True, # overlays the boxplot
        points = "all", #show every point
        hover_data = ["mean_mental_health"],
        color = "diet_quality",
        title = "Diet Quality vs. Mental Health Rating Distribution",
        labels = {"diet_quality": "Diet Quality",
                  "mental_health_rating": "Mental Health Rating"}
    )

    #Creates the the visualization's own layout in the app
    v6_layout = html.Div([
        html.H2("Diet Quality vs. Mental Health Rating"),
        html.P("""Using a violin plot for the visualization, it can be seen that those with good diets
               tend to have the highest average mental health rating (5.65) compared to those with fair or poor mental
               health ratings. Those with fair diets tended to have the lowest average mental health rating
               of only 5.21."""),
        dcc.Graph(figure = fig)
    ])

    return v6_layout