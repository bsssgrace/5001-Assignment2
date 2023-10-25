from dash import dcc, html, Input, Output
from app import app
from apps import q1, q2, q3

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('DADS5001 - Assignment2 | ', href='/'),
        dcc.Link('#1 | ', href='/apps/q1'), # 1
        dcc.Link('#2 | ', href='/apps/q2'), # 2
        dcc.Link('#3 | ', href='/apps/q3') # 3
    ], className="row"),
    html.Div(id='page-content', children=[])
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/q1': # 1
        return q1.layout # 1
    if pathname == '/apps/q2': # 2
        return q2.layout # 2
    if pathname == '/apps/q3': # 3
        return q3.layout # 3
    if pathname == '/':
        return "Please choose above link to have a look on each graph."

if __name__ == '__main__':
    app.run_server(debug=False)

