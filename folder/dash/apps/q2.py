# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# reference: https://python-charts.com/spatial/bubble-map-plotly/

'''
With these two graphs, users can click on each country in one graph and obtain the number of Starbucks stores in each province on another graph.
'''

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from app import app

# read data from csv file
csv_path = 'https://raw.githubusercontent.com/bsssgrace/5001-Assignment2/main/Starbucks.csv'

# prepare data
df2 = pd.read_csv(csv_path).query("(Brand == 'Starbucks') & (Country == 'TH' | Country == 'VN' | Country == 'MY')")
df1_g = df2.groupby(by=["Country"]).count().sort_values(by=["Brand"],ascending=[False]).reset_index() # for fig1
df2_g = df2.groupby(by=["Country", "City"]).count().sort_values(by=["Brand"],ascending=[False]).reset_index() # for fig2

# create the first graph showing values of three countries
fig1 = px.bar(
            df1_g, 
            y="Country",
            x="Brand",
            hover_name='Country',
            hover_data=['Country','Brand'],
            text_auto=True,
            color='Country', # TH, VN, MY
            color_discrete_map={
                    'TH': '#85C1E9',
                    'MY': '#7DCEA0',
                    'VN': '#F7DC6F'},
            title='Number of Starbucks stores by Country')

# remove title
fig1.update_xaxes(title=None)

# adjust legend location
fig1.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="left",
    x=0
))

# Create the second graph showing numbers in each city of the selected country
fig2 = px.bar(title='Number of Starbucks stores by Cities')

# define app layout 
layout = html.Div(children=[

    html.H1(children='Assignment2 #2'),
        html.Div(children=[
                html.P('Instruction: With these two graphs, users can click on each country in one graph and obtain the number of Starbucks stores in each province on another graph.')]),
    html.Div([
        dcc.Graph(id='graph1', figure=fig1),
    ], style={'width': '49%', 'display': 'inline-block'}),
    
    html.Div([
        dcc.Graph(id='graph2', figure=fig2),
    ], style={'width': '49%', 'display': 'inline-block'}),
], style={'padding': 10, 'flex': 1}
)

# define dash callback to update the second graph when a country is clicked on the first graph
@app.callback(
    Output('graph2', 'figure'),
    [Input('graph1', 'clickData')]
    )

def update_graph2(click_data):
    if click_data is not None:
        selected_country = click_data['points'][0]['y']
        filtered_data = df2_g[df2_g['Country'] == selected_country]

        fig2 = px.bar(
                    filtered_data, 
                    y='City', 
                    x='Brand',
                    # text_auto=True,
                    color='Country', # TH, VN, MY
                    color_discrete_map={
                    'TH': '#85C1E9',
                    'MY': '#7DCEA0',
                    'VN': '#F7DC6F'},
                    # title=f'Values of Cities in {selected_country}'
                    title='Number of Starbucks stores by Cities')
        
        # DESC bar by count of store
        fig2.update_layout(yaxis=dict(autorange="reversed"))
        
        # remove title
        fig2.update_xaxes(title=None)

        # adjust legend location
        fig2.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0
        ))
    else:
        fig2 = px.bar(
            df2_g, 
            y="City",
            x="Brand",
            hover_name='City',
            hover_data=['City','Brand'],
            # text_auto=True,
            color='Country', # TH, VN, MY
            color_discrete_map={
                    'TH': '#85C1E9',
                    'MY': '#7DCEA0',
                    'VN': '#F7DC6F'},
            title='Number of Starbucks stores by Cities')
        
        fig2.update_layout(yaxis=dict(autorange="reversed"))
        
        # remove title
        fig2.update_xaxes(title=None)

        # adjust legend location
        fig2.update_layout(legend=dict(
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="left",
        x=0
        ))
    return fig2