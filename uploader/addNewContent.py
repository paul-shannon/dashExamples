from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
from dash.exceptions import PreventUpdate

import base64
import datetime
import io
import pdb

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div(
    id='output',
    children=[
        html.Button("Load more",id='load-new-content',n_clicks=0),
        html.Div("Thing 1")
       ],
)

@app.callback(
    Output('output','children'),
    [Input('load-new-content','n_clicks')],
    [State('output','children')])
def more_output(n_clicks,old_output):
    if n_clicks==0:
        raise PreventUpdate
    return old_output + [html.Div('Thing {}'.format(n_clicks + 1))]

if __name__ == '__main__':
    app.run(debug=True)
