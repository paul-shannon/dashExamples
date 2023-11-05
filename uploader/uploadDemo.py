from dash import Dash, dcc, html, dash_table, Input, Output, State, callback

import xmlFileUtils

import base64
import datetime
import io, os
import pdb

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
messageDivStyle = {"height": 300,
                   "wdith": 600,
                   "border": "1px red solid",
                   "border-radius": 5,
                   "margin": 10,
                   "padding": 10}

app = Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    dcc.Upload(
        id='uploaderWidget',
        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        multiple=False
        ),
    html.Div(id='messageDiv', children=[html.H4("messages")], style=messageDivStyle)
    ])

@callback(Output('messageDiv', 'children', allow_duplicate=True),
          Input('uploaderWidget', 'filename'),
          State('uploaderWidget', 'contents'),
          State('uploaderWidget', 'last_modified'),
          State('messageDiv', 'children'),
          prevent_initial_call=True)
def uploadHandler(filename, content, date, divContents):
  print(filename)
  print(date)
  print(len(content))
  xmlUtils = xmlFileUtils(filename, "tmp", content, verbose=True)
  xmlUtils.saveBytesToFile()
  validEAF = xmlUtils.validateEAF()
  formattedDate = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
  el = html.H4("fubar")
  el = html.Ul(id='list',
               children=[html.Li(filename),
                         html.Li(formattedDate),
                         html.Li(len(content)),
                         html.Li("valid: %s" % validEAF)])
  divContents += [el]
  return divContents

if __name__ == '__main__':
    app.run(debug=True)
