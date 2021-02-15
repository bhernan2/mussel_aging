# -*- coding: utf-8 -*-

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

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
                 #modal for any TXState Alerts
                html.Br(),
                dbc.Container([
                    dbc.Row([
                        html.H5("TX State Alert"),  
                            ],justify="center"),
                        dbc.Button("Open", id='open-center', color="light", size='lg',),        
                            html.Br(),
                            dbc.Row([
                                dbc.Modal([
                                dbc.ModalHeader("Alert"),
                                dbc.ModalBody([
                                    dbc.Card([
                                        # dbc.CardImg(src='assets/_alert.png'),
                                        dbc.CardBody([
                                            html.P("TXState Alert- San Marcos and Round Rock campuses - There is a major winter storm and dangerously cold temperatures anticipated from today through the middle of the week.  Travel conditions are hazardous and very difficult.  Conditions will include ice and snow and reduced visibility.  Power outages are possible due to windy conditions, potential ice accumulation on lines, and a prolonged period of cold temperatures.  Life threatening wind chill temperatures are expected.  Texas State University will be closed through Wednesday, February 17, at 8:00 AM.", className="lead"),
                                            ]),
                                        ]),
                                    ]),
                                dbc.ModalFooter(
                                dbc.Button("Close", id="close-center", size="lg")
                                ),
                            ],
                            id="modal-center",
                            centered=True,
                            size="xl",
                            ),
                            ]),
                        
                    ], id="modal-style" ,fluid=True),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className='sidebar-style',
)
content = html.Div(html.Br(), id="page-content", className='content-style')
homepage = html.Div([
            dbc.Container([
            dbc.Row([ 
                html.H1("Stream Ecology Project Tracking", className="display-4"),
                html.Br(),
                html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                ]),
            ],fluid=True, style={'textAlign': 'left'}),
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
            html.Br(),
            ],fluid=True, className='cards'),
        ])



footer = html.Footer(
    html.P('Copyright © 2021 BAH - All Rights Reserved.'), id="footer", className='footer-style')

def Dashboard():
    layout= html.Div([
    dcc.Location(id="url"), 
    sidebar, 
    content,
    #footer])
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA])
server = app.server
app.layout = Dashboard()


#modal callback
@app.callback(
    Output("modal-center", "is_open"),
    [Input("open-center", "n_clicks"), Input("close-center", "n_clicks")],
    [State("modal-center", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return homepage
    elif pathname == "/page-1":
        return html.Div([
            dbc.Container([
                dbc.Row([ 
                    html.H1("Aging project", className="display-4"),
                    html.Br(),
                    html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                    ]), 
                    html.Br(),
                dbc.Row([
                    html.P("Project info: ", className="lead")
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

