import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly
import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import numpy as np

from datetime import datetime


app = dash.Dash(external_stylesheets=[dbc.themes.LITERA])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "28rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "30rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Stream ecology lab: project tracking", className="display-4"),
        html.Hr(),
        html.P(
            "", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Aging", href="/", active="exact"),
                html.Br(),
                dbc.NavLink("Project 2", href="/page-1", active="exact"),
                html.Br(),
                dbc.NavLink("Project 3", href="/page-2", active="exact"),
                
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([
            dbc.Row([ 
                html.H1("Aging project", className="display-4"),
            ])   
        ])
    elif pathname == "/page-1":
        return html.Div([
            dbc.Row([ 
                html.H1("Project 2", className="display-4"),
            ])   
        ])
    elif pathname == "/page-2":
        return html.Div([
            dbc.Row([ 
                html.H1("Project 3", className="display-4"),
            ])   
        ])
    # If the user tries to reach a different page, return a 404 message
    


if __name__ == "__main__":
    app.run_server(debug=True)
