import pandas as pd
import plotly.express as px



df = pd.read_csv('database.csv')

def exam_scores_hist():
    """The exam_scores_hist method creates a histogram that shows
    the variation of the scores in the database. No args or returns needed.
    """
    fig = px.histogram(df, x = "exam_score", title = "Exam Score Distribution")

    return fig