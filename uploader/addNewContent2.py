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
      # html.Div("Thing 1"),
      html.Div(id="dynamicDiv", children=[html.Span("")], style=dynamicDivStyle)
      ],
   )

@app.callback(
    Output('dynamicDiv',       'children'),
    [Input('load-new-content', 'n_clicks')],
    [State('dynamicDiv',       'children')])
def more_output(n_clicks, divContents):
    if n_clicks==0:
        raise PreventUpdate
    #print("--- old_output:")
    #print(old_output)
    #pdb.set_trace()
    divContents += [html.P('Thing {}'.format(n_clicks + 1))]
    return divContents #+ [html.P('Thing {}'.format(n_clicks + 1))]
    #if old_output:
    #   newOutput = old_output.append(html.Div('Thing {}'.format(n_clicks + 1)))
    #   return newOutput

if __name__ == '__main__':
    app.run(debug=True)
