# Run this app with `python app_main.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
from dash import dcc, html
from exam_scores import exam_scores_hist

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Testing Dashboard"),
    dcc.Graph(figure = exam_scores_hist())
])

if __name__ == "__main__":
    app.run(debug = True)