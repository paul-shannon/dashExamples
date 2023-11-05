from dash import Dash, dcc, html, dash_table, Input, Output, State, callback

import base64
import datetime
import io

import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Store(id='storage', storage_type='memory'),
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        style={
            'width': '40%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'solid',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
            },
        multiple=False
        ),
    html.Button('Check', id='check-eaf-button', n_clicks=0),
    html.Button('Storage', id='store-values-button', n_clicks=0),
    html.Div(id='outputmessages')
    ])

@callback(Output("storage", 'data'),
          Input("store-values-button", "value"),
          prevent_initial_call=True)
def updateStorage(newData, value):
    print("updateStorage")
    print(value)
    return value.to_json()

@callback(Output('outputmessages', 'children', allow_duplicate=True),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'),
          prevent_initial_call=True)
def update_output(list_of_contents, list_of_names, list_of_dates):
  if list_of_names:
        return list_of_names

@callback(
    Output('outputmessages', 'children', allow_duplicate=True),
    Input('storage', 'data'),
    prevent_initial_call=True
)
def update_output(data):
    print("check eaf")
    return(data)






if __name__ == '__main__':
    app.run(debug=True)
