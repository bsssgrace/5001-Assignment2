# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

'''
With this graph, users can compare the number of Starbucks stores among Thailand, Vietnam and Malaysia.
'''

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from app import app
import plotly.io as pio

# change theme
pio.templates.default = "plotly_white"

# read data from csv file
csv_path = 'https://raw.githubusercontent.com/bsssgrace/5001-Assignment2/main/Starbucks.csv'

# prepare data
df1 = pd.read_csv(csv_path).query("(Brand == 'Starbucks') & (Country == 'TH' | Country == 'VN' | Country == 'MY')")
df1_g = df1.groupby(by=["Country"]).count().sort_values(by=["Brand"],ascending=[False]).reset_index()

# graph
fig1 = px.bar(
                df1_g, 
                x="Brand",
                y='Country',
                color='Country', # TH, MY, VN
                color_discrete_map={
                    'TH': '#85C1E9',
                    'MY': '#7DCEA0',
                    'VN': '#F7DC6F'},
                title='Number of Starbucks stores among Thailand, Vietnam and Malaysia<br><sup>Apart from Starbucks, other coffee/tea stores are not available in Thailand, Vietnam and Malaysia according to the Starbucks raw dataset.</sup>',
                text_auto=True
                )

# remove title (x)
fig1.update_xaxes(title=None)

# adjust legend location
fig1.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="left",
    x=0
))

layout = html.Div(children=[

      html.H1(children='Assignment2 #1'),
        html.Div(children=[
            html.P('Instruction: A graph with one component. With this graph, users can compare the number of Starbucks stores among Thailand, Vietnam and Malaysia.')
            ]),

        dcc.Graph(
            id='bar1',
            figure=fig1
        ),
    
     ], style={'padding': 10, 'flex': 1})