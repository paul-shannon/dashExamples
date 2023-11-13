from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
from dash.exceptions import PreventUpdate

import base64
import datetime
import io
import pdb

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dynamicDivStyle = {"width": 400,
                   "border": "1px solid darkblue",
                   "border-radius": 5,
                   "margin": 10,
                   "padding": 10}

app = Dash(__name__, external_stylesheets=external_stylesheets)

# the dynamic div's children must be a list, so that it can be
# note that list += [newItem] is equivalent to list.append(newItem)

app.layout=html.Div(
   id='output',
   children=[
      html.Button("Load more",id='load-new-content',n_clicks=0),
      dcc.Upload(
        id='uploaderWidget',
        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        multiple=False
        ),
      html.Div("Thing 1"),
       html.Div(id="dynamicDiv", children=[html.Span("")], style=dynamicDivStyle),
      html.Div(id="uploadOutputDiv", children=[html.Span("")], style=dynamicDivStyle)
      ],
   )

@app.callback(
    Output('dynamicDiv',       'children'),
    [Input('load-new-content', 'n_clicks')],
    [State('dynamicDiv',       'children')])
def clickHandler(n_clicks, divContents):
    if n_clicks==0:
        raise PreventUpdate
    divContents += [html.P('Thing {}'.format(n_clicks + 1))]
    return divContents

@app.callback(
    Output('uploadOutputDiv',   'children'),
    Input('uploaderWidget',   'filename'),
    State('dynamicDiv',       'children'),
    State('uploaderWidget',   'contents'))
def uploadHandler(filename, divContents, contents):
    if filename == None:
        raise PreventUpdate
    divContents += [html.P(filename)]
    divContents += [html.P(len(contents))]
    return divContents



if __name__ == '__main__':
    app.run(debug=True)
