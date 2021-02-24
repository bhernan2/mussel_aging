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

from figures import aging_boxplot, zebra_burrow_scatter, zebra_burrow_boxplot

#sidebar 
sidebar = html.Div([
        html.H2("home & projects", className="display-6"),
        html.Hr(),
        dbc.Nav(
            [
                html.Br(),
                dbc.NavLink("Home", href="/", active="exact"),
                html.Br(),
                dbc.NavLink("Meet the lab", href="/page-1", active="exact"),
                html.Br(),
                dbc.NavLink("Aging", href="/page-2", active="exact"),
                html.Br(),
                dbc.NavLink("USACE", href="/page-3", active="exact"),
                html.Br(),
                dbc.NavLink("Summer", href="/page-4", active="exact"),
                html.Br(),
                dbc.NavLink("Zebra mussels", href="/page-5", active="exact"),
                html.Br(),
                
                html.Br(),
                html.Br(),
                html.Br(),
                html.Br(),
                #modal for any TXState Alerts
                # dbc.Container([
                #     dbc.Row([
                #         html.H5("TX State Alert"),  
                #             ],justify="center"),
                #         dbc.Row([
                #         dbc.Button("Open", id='open-center', color="danger", className="mr-1", size="lg"),
                #         ], justify="center"),  
                #     html.Br(),
                #             dbc.Row([
                #                 dbc.Modal([
                #                 dbc.ModalHeader("Alert"),
                #                 dbc.ModalBody([
                #                     dbc.Card([
                #                         # dbc.CardImg(src='assets/_alert.png'),
                #                         dbc.CardBody([
                #                             html.P("Texas State University will be closed through 8:00 a.m. on Wednesday, February 24, 2021. due to inclement weather and continued power outages which have impacted multiple university systems, including phone lines and computer networks. All classes and events are canceled, including virtual/online classes and events. University offices will remain closed. Only designated critical personnel should report to work on the campuses.", className="lead"),
                #                             ]),
                #                         ]),
                #                     ]),
                #                 dbc.ModalFooter(
                #                 dbc.Button("Close", id="close-center")
                #                 ),
                #             ],
                #             id="modal-center",
                #             centered=True,
                #             size="lg",
                #             ),
                #             ]),
                        
                #     ], id="modal-style" ,fluid=True),
                #turn modal off when there is not an annoucement 
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className='sidebar-style',
)
#content for pages adjacent to sidebar
content = html.Div(html.Br(), id="page-content", className='content-style')

#homepage
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

#dropdown jumbo
dropdown = html.Div([
    html.Br(),
    dbc.Row([
        html.H3("Explore the data", className='text-center', ),
        ]),
    dbc.Row([
        dcc.Dropdown(
            id='aging-dropdown', 
            clearable=False,
            style={'backgroundColor': '#fffff', 'color':'black', 'width': '100%'},
            options=[
                    # {'label': 'Histogram', 'value': 'plot1-info'},
                    {'label': 'Boxplot', 'value': 'plot2-info'},
                    # {'label': 'Linear regression', 'value': 'plot3-info'},
                    # {'label': 'Analysis', 'value': 'plot4-info'},       
                    ],
            placeholder='Select'
                )
        ],justify="center"),
    dbc.Row(id='dd-output-container', justify="center"),
])

#dropdown jumbo
dropdown2 = html.Div([
    html.Br(),
    dbc.Row([
        html.H3("Explore projects", className='text-center', ),
        ]),
    dbc.Row([
        dcc.Dropdown(
            id='zebra-dropdown', 
            clearable=False,
            style={'backgroundColor': '#fffff', 'color':'black', 'width': '100%'},
            options=[
                    {'label': 'Burrowing', 'value': 'plot1-info'},       
                    ],
            placeholder='Select a project'
                )
        ],justify="center"),
    dbc.Row(id='dd-output-container2', justify="center"),
])

aging = html.Div([
            dbc.Container([
                dbc.Row([ 
                    html.H1("Aging project", className="display-4"),
                    html.Br(),
                    html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                    ]), 
                    html.Br(),
                dbc.Row([
                    html.P("Project info: a few sentences explaining projects", className="lead")
                    ]),  
                html.Br(),
                dbc.Row([
                    #include drowdown for figures
                    dbc.Col([
                        dropdown
                        ]),
                    ]),                     
            ],fluid=True, style={'textAlign': 'left'}),     
        ])
zebra = html.Div([
            dbc.Container([
                dbc.Row([ 
                    html.H1("Zebra mussel projects", className="display-4"),
                    html.Br(),
                    html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                    ]),
                    html.Br(),
                dbc.Row([
                    html.P("Project info: a few sentences explaining projects", className="lead")
                    ]), 
                html.Br(),   
                dbc.Row([
                    dbc.Col([dropdown2,]),    
                ]),                   
            ],fluid=True, style={'textAlign': 'left'}),     
        ])
    
footer = html.Div([
    html.Footer( html.P('Copyright © 2021 BAH - All Rights Reserved.'), id="footer", className='footer-style'),
    ])



def Dashboard():
    layout= html.Div([
    dcc.Location(id="url"), 
    sidebar, 
    content,
    footer
    ])
    return layout

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.LITERA])
server = app.server
app.layout = Dashboard()


#modal callback
# @app.callback(
#     Output("modal-center", "is_open"),
#     [Input("open-center", "n_clicks"), Input("close-center", "n_clicks")],
#     [State("modal-center", "is_open")],
# )
# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return homepage
    
    elif pathname == "/page-1":
        return html.Div([
            dbc.Container([
                dbc.Row([ 
                    html.H1("Meet the lab members", className="display-4"),
                    html.Br(),
                    # html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                    ]),                     
            ],fluid=True, style={'textAlign': 'left'}),     
        ])
       
    elif pathname == "/page-2":
        return aging

    elif pathname == "/page-3":
        return html.Div([
            dbc.Container([
                dbc.Row([ 
                    html.H1("USACE project", className="display-4"),
                    html.Br(),
                    html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                    ]),                     
            ],fluid=True, style={'textAlign': 'left'}),     
        ])
    elif pathname == "/page-4":
        return html.Div([
            dbc.Container([
                dbc.Row([ 
                    html.H1("Summer project", className="display-4"),
                    html.Br(),
                    html.P("Description: This space will monitor and track the status of ongoing projects for the stream ecology lab. It will include interactive maps, charts, figures and summaries.", className="lead"),
                    ]),                     
            ],fluid=True, style={'textAlign': 'left'}),     
        ])
    elif pathname == "/page-5":
        return zebra
#aging dropdown figures callbacks
@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('aging-dropdown', 'value')])
def update_plot(value):
    if value == "plot2-info":
        return html.Div([
                    dbc.Col([
                        dcc.Graph(
                            figure = aging_boxplot(),
                            id='plot2', 
                            config={
                                'displayModeBar': False, 
                                'responsive': True, 
                                'autosizable':True,
                                #'fillFrame':True 
                                },
                            style={'display': 'flex', 'vertical-direction': 'column',},),
                            #{ display: flex; flex-direction: column; }                      
                        ], align="center",),
                        #width={"sm": 12, "md": {"size": 12, "order": 6}, "lg":12},           
        ])
#zebra dropdown figures callbacks
@app.callback(
    dash.dependencies.Output('dd-output-container2', 'children'),
    [dash.dependencies.Input('zebra-dropdown', 'value')])
def update_plot(value):
    if value == "plot1-info":
        return html.Div([
            dbc.Row([
                    dbc.Col([
                        html.Br(),
                        html.P('Counts of A. plicata mussels burrowed at ~90% by tanks (T1 ... T12) across days.', className='lead'),
                        dcc.Graph(
                            figure = zebra_burrow_scatter(),
                            id='plot1', 
                            config={
                                'displayModeBar': False, 
                                'responsive': True, 
                                'autosizable':True,
                                #'fillFrame':True 
                                },
                            style={'display': 'flex', 'vertical-direction': 'column',},),
                            #{ display: flex; flex-direction: column; }                      
                        ], align="center", width=7),
                        #width={"sm": 12, "md": {"size": 12, "order": 6}, "lg":12},
                    dbc.Col([
                        html.Br(),
                        html.P('ANOVA', className='lead')
                    ], align='top', width=5),
            ]), 
            dbc.Row([
                    dbc.Col([
                        html.P('Boxplots of A. plicata control (no zebra mussels) and treatment (zebra mussels present & zebra mussels attached) tanks. The ends of the box represent the lower and upper quartiles, while the median (second quartile) is marked by a line inside the box.', className='lead'),
                        dcc.Graph(
                            figure = zebra_burrow_boxplot(),
                            id='plot2', 
                            config={
                                'displayModeBar': False, 
                                'responsive': True, 
                                'autosizable':True,
                                #'fillFrame':True 
                                },
                            style={'display': 'flex', 'vertical-direction': 'column',},),
                            #{ display: flex; flex-direction: column; }                      
                        ], align="center", width = 7),
                    dbc.Col([
                        html.P("Tukey HSD", className="lead")
                    ], align='top', width=5),
                        #width={"sm": 12, "md": {"size": 12, "order": 6}, "lg":12},
            ]),   
        ])
    # elif value == 'plot1-info':
    #     return html.Div([
    #         dbc.Row([
    #                 dbc.Col([
    #                     html.H6('L. teres'),
    #                     dcc.Graph(
    #                         #figure = ,
    #                         id='plot1', 
    #                         config={
    #                             'displayModeBar': False, 
    #                             'responsive': True, 
    #                             #'autosizable':True,
    #                             #'fillFrame':True 
    #                             },
    #                         style={'display': 'inline-block', 'vertical-align': 'middle'}),                      
    #                     ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
    #         ])
    #     ])
    # elif value == 'plot3-info':
    #     return html.Div([
    #         dbc.Row([
    #                 dbc.Col([
    #                     html.H6('L. teres'),
    #                     dcc.Graph(
    #                         #figure = ,
    #                         id='plot3', 
    #                         config={
    #                             'displayModeBar': False, 
    #                             'responsive': True, 
    #                             #'autosizable':True,
    #                             #'fillFrame':True 
    #                             },
    #                         style={'display': 'inline-block', 'vertical-align': 'middle'}),                      
    #                     ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
    #         ])
    #     ])
    # elif value == 'plot4info':
    #     return html.Div([
    #         dbc.Row([
    #                 dbc.Col([
    #                     html.H6('L. teres'),
    #                     dcc.Graph(
    #                         #figure = ,
    #                         id='plot4', 
    #                         config={
    #                             'displayModeBar': False, 
    #                             'responsive': True, 
    #                             #'autosizable':True,
    #                             #'fillFrame':True 
    #                             },
    #                         style={'display': 'inline-block', 'vertical-align': 'middle'}),                      
    #                     ], width={"sm": 12, "md": {"size": 6, "order": 1}, "lg":4},),
    #         ])
    #     ])
       


if __name__ == "__main__":
    app.run_server(debug=True)

