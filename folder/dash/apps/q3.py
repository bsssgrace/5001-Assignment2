# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
# reference: https://python-charts.com/spatial/bubble-map-plotly/

'''
Map graph, With this map graph, users can pick (using the UI) and see the density of Starbucks stores in each big city in Thailand (Bangkok, Phuket and Chiangmai).
'''

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd
from app import app

# read data from csv file
csv_path = 'https://raw.githubusercontent.com/bsssgrace/5001-Assignment2/main/Starbucks.csv'

# prepare data by filtering data to have 3 big cities in Thailand
df3 = pd.read_csv(csv_path).query("(Brand == 'Starbucks') & (Country == 'TH') & (City == 'Bangkok' | City == 'Phuket' | City == 'Chiangmai')")
df = pd.DataFrame(df3)
cities_to_show = ["Bangkok","Phuket","Chiangmai"]

# create a scatter mapbox plot by using the filtered data of 3 big cities in Thailand
fig_map = px.scatter_mapbox(
                            data_frame=df, 
                            lat='Latitude', 
                            lon='Longitude',
                            hover_name='City',
                            hover_data={'City': True},
                            title='Number of Starbucks stores in 3 big cities (Bangkok, Phuket and Chiangmai) in Thailand',
                            zoom=8, 
                            mapbox_style='open-street-map')

# create a dropdown to select each city
city_dropdown = dcc.Dropdown(
    id='city-dropdown',
    options=[
        {'label': city, 'value': city} for city in cities_to_show
    ],
    value=cities_to_show[0],  # default value
    style={'width': '30%'}
)

layout = html.Div(children=[

        html.H1(children='Assignment2 #3'),
            html.Div(children=[
                html.P('Instruction: With this map graph, users can pick (using the UI) and see the density of Starbucks stores in each big city in Thailand (Bangkok, Phuket and Chiangmai).')
            ]),

        city_dropdown, # add dropdown to the layout

        dcc.Graph(id='map3', figure=fig_map),
        ], 
        style={'padding': 10, 'flex': 1})

# define a callback to update the map based on the selected city from the dropdown
@app.callback(
    Output('map3', 'figure'),
    [Input('city-dropdown', 'value')]
)

def update_map(selected_city):

    # filter dataframe based on the selected city
    filtered_data = df[df['City'] == selected_city] 

    # create a new scatter mapbox plot for the selected city
    fig_map_updated = px.scatter_mapbox(
                        data_frame=filtered_data, 
                        lat='Latitude', 
                        lon='Longitude', 
                        hover_name='City',
                        hover_data={'City': True},
                        zoom=8, 
                        mapbox_style='open-street-map',
                        title='Number of Starbucks stores in 3 big cities (Bangkok, Phuket and Chiangmai) in Thailand <br><sup>This graph will present only the density of Starbucks stores in each big city in Thailand.</sup>'
                        # title=f'Starbucks Stores Density in {selected_city} <br><sup>This graph will present only the density of Starbucks stores in each big city in Thailand.</sup>'
                        )
    
    return fig_map_updated


