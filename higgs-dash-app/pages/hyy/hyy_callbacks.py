from dash.dependencies import Input, Output
import plotly.express as px
from app import app
from pages.hyy.hyy_data import hyy_dataframe


@app.callback(
    Output('hyy-graph', 'figure'),
    Input('myy-slider', 'value'))
def update_figure(selected_value):
    hyy_df = hyy_dataframe()
    filtered_df = hyy_df[hyy_df.myy == selected_value]

    fig = px.scatter(
                    filtered_df, 
                    x="photon_isTightID", 
                    y="myy"
                    )
                    #size="pop", 
                    #color="continent", 
                    #hover_name="country",
                    #log_x=True, 
                    #size_max=55)
    fig.update_layout(transition_duration=500)

    return fig