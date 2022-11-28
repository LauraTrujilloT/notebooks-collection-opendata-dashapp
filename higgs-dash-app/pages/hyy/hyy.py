from dash import html
from dash import dcc
from pages.hyy.hyy_data import hyy_dataframe

layout = html.Div([
    html.H1("HYY Analysis"),
    html.Hr(),
    html.Iframe(
                id='hyy-graph', 
                srcDoc=None,
                style={'border-width': '5', 'width': '100%',
                       'height': '500px'}
                ),
    dcc.Slider(
        id='myy-slider',
        min=hyy_dataframe()['myy'].min(),
        max=hyy_dataframe()['myy'].max(),
        value=hyy_dataframe()['myy'].min(),
        marks={str(myy): str(myy) for myy in hyy_dataframe()['myy'].unique()},
        step=None
    )
])