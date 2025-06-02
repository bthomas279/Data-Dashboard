#This script puts the other scripts together into one
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import html
from exam_scores import exam_scores
from media_vs_sleep import media_vs_sleep
from study_vs_media import gender_work_social

app = dash.Dash(__name__)

#Create the final layout
app.layout = html.Div([
    html.H1("Dash App Dashboard"),
    exam_scores(),
    html.Hr(),
    media_vs_sleep(),
    html.Hr(),
    gender_work_social(),
])

if __name__ == "__main__":
    app.run(debug = True)