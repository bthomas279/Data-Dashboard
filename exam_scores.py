import pandas as pd
import plotly.express as px

df = pd.read_csv('database.csv')

def exam_scores_hist():
    fig = px.histogram(df, x = "City", title = "Exam Score Distribution")

    return fig