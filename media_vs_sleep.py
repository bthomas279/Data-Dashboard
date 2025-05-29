#This script is for making the social media hours vs sleep visualization
import plotly.express as px
import pandas as pd

df = pd.read_csv('database.csv')

def media_vs_sleep():
    fig = px.histogram(df, x = ""

