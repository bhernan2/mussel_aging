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

sidebar = html.Div([
        html.H2("home & projects", className="display-6"),
        html.Hr(),
        dbc.Nav(
            [
                html.Br(),
                dbc.NavLink("Home", href="/", active="exact"),
                html.Br(),
                dbc.NavLink("Aging", href="/page-1", active="exact"),
                html.Br(),
                dbc.NavLink("USACE", href="/page-2", active="exact"),
                html.Br(),
                dbc.NavLink("Summer", href="/page-3", active="exact"),
                html.Br(),
                dbc.NavLink("Zebra mussels", href="/page-4", active="exact"),
                # html.Img(src='assets/mussel_foot.jpg', style=IMG_STYLE)
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className='sidebar-style',
)

content = html.Div(id="page-content", className='content-style')

footer = html.Footer(id="footer", className='footer-style')

def Dashboard():
    layout= html.Div([
    dcc.Location(id="url"), 
    sidebar, 
    content,
    footer])
    return layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA])
server = app.server
app.layout = Dashboard()

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.Div([
            dbc.Container([
            dbc.Row([ 
                html.H1("Stream Ecology Project Tracking", className="display-4"),
                html.Br(),
                html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                ]),
            ],fluid=True ),
            html.Br(),
            dbc.Container([      
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("Aging project"),
                                dbc.CardImg(src="/assets/___aging.jpg"),
                                ])
                            ], className="flip-card-front", color="", inverse=False, style={"display": "flex"}),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4('Important dates:', style={'font-weight': 'bold'}),
                                html.H4('To do:', style={'font-weight': 'bold'}),
                                html.P('Pairwise comparison between agers', className='lead'),
                                
                                ]),
                            ],className="flip-card-back", color="", inverse=False)
                    ],className="flip-card-inner",), 
                ],className="flip-card"),
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("USACE project"),
                                dbc.CardImg(src="/assets/_usace.png"),
                                ])
                            ], className="flip-card-front", color="", inverse=False, style={"display": "flex"}),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4('Important dates', style={'font-weight': 'bold'})
                                ]),
                            ],className="flip-card-back", color="", inverse=False)
                    ],className="flip-card-inner",), 
                ],className="flip-card"),
                
                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("Summer project"),
                                dbc.CardImg(src="/assets/_musseling.jpg"),
                                ])
                            ], className="flip-card-front", color="", inverse=False, style={"display": "flex"}),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4('Important dates', style={'font-weight': 'bold'})
                                ]),
                            ],className="flip-card-back", color="", inverse=False)
                    ],className="flip-card-inner",), 
                ],className="flip-card"),

                dbc.Row([
                    dbc.Col([
                        dbc.Card([
                            dbc.CardBody([
                                html.H4("Zebra mussels project"),
                                dbc.CardImg(src="/assets/_zebra.jpg"),
                                ])
                            ], className="flip-card-front", color="", inverse=False, style={"display": "flex"}),
                        dbc.Card([
                            dbc.CardBody([
                                html.H4('Important dates', style={'font-weight': 'bold'})
                                ]),
                            ],className="flip-card-back", color="", inverse=False)
                    ],className="flip-card-inner",), 
                ],className="flip-card"),
            
                ],fluid=True, className='cards'),
            ])
    elif pathname == "/page-1":
        return html.Div([
            dbc.Container([
                dbc.Row([ 
                    html.H1("Aging project", className="display-4"),
                    html.Br(),
                    html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                    ]),                     
            ],fluid=True, style={'textAlign': 'left'}),     
        ])
    elif pathname == "/page-2":
        return html.Div([
            dbc.Container([
                dbc.Row([ 
                    html.H1("USACE project", className="display-4"),
                    html.Br(),
                    html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                    ]),                     
            ],fluid=True, style={'textAlign': 'left'}),     
        ])
    elif pathname == "/page-3":
        return html.Div([
            dbc.Container([
                dbc.Row([ 
                    html.H1("Summer project", className="display-4"),
                    html.Br(),
                    html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                    ]),                     
            ],fluid=True, style={'textAlign': 'left'}),     
        ])
    elif pathname == "/page-4":
        return html.Div([
            dbc.Container([
                dbc.Row([ 
                    html.H1("Zebra mussels project", className="display-4"),
                    html.Br(),
                    html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                    ]),                     
            ],fluid=True, style={'textAlign': 'left'}),     
        ])

if __name__ == "__main__":
    app.run_server(debug=True)

