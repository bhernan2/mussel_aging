import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import sys

from definitions import SIDEBAR, CONTENT

_sidebar = SIDEBAR()
_content = CONTENT()

def dashboard():
    layout = html.Div([
        dcc.Location(id="url"),
        _sidebar,
        _content
    ])
    return layout

app = dash.Dash(__name__, external_stylesheets = [dbc.themes.BOOTSTRAP])

app.layout = dashboard()

#space for app callbacks 
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("Aging project!")
    elif pathname == "/page-1":
        return html.P("Another project!")
    elif pathname == "/page-2":
        return html.P("Another project!")
    

server = app.server
if __name__ == "__main__":
    app.run_server(debug=True)