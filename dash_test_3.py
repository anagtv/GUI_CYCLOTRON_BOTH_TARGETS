import json
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output,State
import plotly.express as px
import pandas as pd
import tfs
import base64
import datetime
import dash_table
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go


df_summary_source = tfs.read("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/20210625/table_summary_source.out")
df_summary_vacuum = tfs.read("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/20210625/table_summary_vacuum.out")
df_summary_beam = tfs.read("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/20210625/table_summary_beam.out")
df_summary_rf = tfs.read("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/20210625/table_summary_rf.out")
df_summary_performance = tfs.read("/Users/anagtv/Documents/OneDrive/046 - Medical Devices/Mantenimientos ciclotrones/TCP/ANALYSIS/20210625/source_summary_values.out")
df = pd.DataFrame(list(zip(df_summary_beam.DATE,df_summary_source.CURRENT_AVE,df_summary_source.CURRENT_STD,df_summary_beam.TARGET_CURRENT_AVE,df_summary_beam.TARGET_CURRENT_STD,df_summary_beam.COLL_CURRENT_L_AVE + df_summary_beam.COLL_CURRENT_R_AVE,
	df_summary_beam.COLL_CURRENT_L_STD + df_summary_beam.COLL_CURRENT_R_STD,df_summary_vacuum.PRESSURE_AVE))
    ,columns=["DATE","SOURCE","SOURCE_STD","TARGET","TARGET_STD","COLLIMATORS","COLLIMATORS_STD","VACUUM"])
df_target_1 = tfs.read("cumulated_charge_1.out")
df_target_2 = tfs.read("cumulated_charge_2.out")
columns = ["SOURCE","VACUUM","RF"]


#fig_evolution.write_html('first_figure.html', auto_open=True)

content_first_row = dbc.Row(
    [
        dbc.Col(
            dbc.Row([dcc.Graph(id='time-series-chart')])
        ),
       dbc.Col(
            dbc.Row([dcc.Graph(id='time-series-chart3'),dcc.Graph(id='time-series-chart4')])
        )
    ]
)


app = dash.Dash(__name__)

app.layout = html.Div([
    dbc.Container([dbc.Row([dcc.Dropdown(
        id="ticker",
        options=[{"label": x, "value": x} 
                 for x in columns],
        value=df.columns[1],
        clearable=False,
    )]),
    content_first_row
    ])
])


@app.callback(
    Output("time-series-chart4", "figure"), 
    [Input("ticker", "value")])
def display_source_performance(ticker):
    if ticker == "SOURCE": 
        df_to_average = df_summary_performance.PERFORMANCE
    elif ticker == "VACUUM":
        df_to_average = df_summary_vacuum['PRESSURE_AVE']
    else: 
        df_to_average = df_summary_rf.FORWARD_POWER_AVE
    fig_evolution = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = np.average(df_to_average) ,
    domain = {'x': [0, 1], 'y': [0, 1]},
    title = {'text': "Source performance [mA/\u03bcA]"},
    gauge = {
                'axis': {'range': [None, 5], 'tickwidth': 1, 'tickcolor': "darkblue"},
                'bar': {'color': "darkblue"},
                'steps' : [
                     {'range': [0, 1.5], 'color': "green"},
                     {'range': [1.5, 3], 'color': "yellow"},
                     {'range': [3, 4.5], 'color': "orange"},
                     {'range': [4.5, 6], 'color': "red"}
                ],
        
                'threshold' : {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 3.5}
            }
))
    fig_evolution.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
    return fig_evolution


#@app.callback(
#    Output("time-series-chart2", "figure"), 
#    [Input("ticker", "value")])
#def display_time_series_2(ticker):
#    fig3 =go.Figure(go.Sunburst(
#     labels=["Target 1", "Foil 1 (1)", "Foil 2 (1)", "Foil 3 (1)"],
#    parents=["","Target 1","Target 1","Target 1","Target 1","Target 1","Target 1"],values = [df_target_1.CURRENT_TARGET.sum(), df_target_1.CURRENT_FOIL[df_target_1.FOIL == "1"].sum(), df_target_1.CURRENT_FOIL[df_target_1.FOIL == "2"].sum(), df_target_1.CURRENT_FOIL[df_target_1.FOIL == "3"].sum()]))
#    fig3.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
#    return fig3

@app.callback(
    Output("time-series-chart3", "figure"), 
    [Input("ticker", "value")])
def display_time_series_2(ticker):
    fig2 =go.Figure(go.Sunburst(
     labels=["Total", "Target 1", "Target 2", "Foil 1 (1)","Foil 2 (1)", "Foil 3 (1)","Foil 4 (1)","Foil 5 (1)","Foil 6 (1)","Foil 1 (2)","Foil 2 (2)", "Foil 3 (2)"],
    parents=["","Total","Total","Target 1","Target 1","Target 1","Target 1","Target 1","Target 1","Target 2","Target 2","Target 2"],values = [df_target_1.CURRENT_TARGET.sum() + df_target_2.CURRENT_TARGET.sum(),df_target_1.CURRENT_TARGET.sum(),df_target_2.CURRENT_TARGET.sum(),
    df_target_1.CURRENT_FOIL[df_target_1.FOIL == "1"].sum(), df_target_1.CURRENT_FOIL[df_target_1.FOIL == "2"].sum(), df_target_1.CURRENT_FOIL[df_target_1.FOIL == "3"].sum(),
    df_target_1.CURRENT_FOIL[df_target_1.FOIL == "1"].sum(), df_target_1.CURRENT_FOIL[df_target_1.FOIL == "2"].sum(), df_target_1.CURRENT_FOIL[df_target_1.FOIL == "3"].sum(),
    df_target_2.CURRENT_FOIL[df_target_2.FOIL == "1"].sum(), df_target_2.CURRENT_FOIL[df_target_2.FOIL == "2"].sum(), df_target_2.CURRENT_FOIL[df_target_2.FOIL == "3"].sum()]))
    fig2.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})
    return fig2

@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    if ticker == "SOURCE":
    	y_values = [df['SOURCE'],df['TARGET'],df['COLLIMATORS']]
    	y_values_error =  [df['SOURCE_STD'],df['TARGET_STD'],df['COLLIMATORS_STD']]
    	names = ["I source","I target","I collimators"]
    	units = [r"I [mA]","I [\u03bcA]","I [\u03bcA]"]
    elif ticker == "VACUUM":
    	y_values = [df['SOURCE'],df_summary_vacuum['PRESSURE_AVE'],df_summary_source['HFLOW'].astype(float)] 
    	y_values_error =  [df['SOURCE_STD'],df_summary_vacuum['PRESSURE_STD'],[0]*len(df_summary_source['HFLOW'].astype(float))]
    	names = ["Source","Pressure","Gas flow"]
    	units = ["I [mA]","10e-5 mbar","sccm"]
    else: 
    	y_values = [df['SOURCE'],df_summary_rf['DEE1_VOLTAGE_AVE'],df_summary_rf['FORWARD_POWER_AVE']]
    	y_values_error =  [df['SOURCE_STD'],df_summary_rf['DEE1_VOLTAGE_STD'],df_summary_rf['FORWARD_POWER_STD']]
    	names = ["Source","RF Power", "RF Voltage"]
    	units = ["I [mA]","kW","kV"]
    fig = make_subplots(rows=3, cols=1,shared_xaxes=True,
                    vertical_spacing=0.02)
    fig.add_trace(go.Scatter(x=df['DATE'], y=y_values[0],mode='markers',                                                         
    marker=go.Marker(color='#3D3C28'),
    	error_y=dict(
            type='data',
            symmetric=True,
            array=y_values_error[0],
            ),name=names[0]),row=1, col=1)
    fig.add_trace(go.Scatter(x=df['DATE'], y=y_values[1],error_y=dict(
            type='data',
            symmetric=True,
            array=y_values_error[1],
            ),name=names[1]),row=2, col=1)
    fig.add_trace(go.Scatter(x=np.array(df.DATE), y=y_values[2],
    	error_y=dict(
            type='data',
            symmetric=True,
            array=y_values_error[2],
            ),name=names[2]),row=3, col=1)
    fig.update_layout(height=900, width=800)
    fig.update_xaxes(title_text="Date", row=3, col=1)
    fig.update_yaxes(title_text=units[0], row=1, col=1)
    fig.update_yaxes(title_text=units[1], row=2, col=1)
    fig.update_yaxes(title_text=units[2], row=3, col=1)
    return fig



app.run_server(debug=True)