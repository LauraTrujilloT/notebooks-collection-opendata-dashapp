#import dash_html_components as html
from dash import html
from dash import dcc
#import dash_core_components as dcc

from layout.sidebar.sidebar import sidebar


content = html.Div(id="page-content")

layout = html.Div([dcc.Location(id="url"), sidebar, content])