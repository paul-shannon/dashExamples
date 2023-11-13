from dash import Dash, dcc, html, dash_table, Input, Output, State, callback
from dash.exceptions import PreventUpdate

import base64
import datetime
import io
import pdb

from xmlFileUtils import XmlFileUtils

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
dynamicDivStyle = {"width": 400,
                   "border": "1px solid darkblue",
                   "border-radius": 5,
                   "margin": 10,
                   "padding": 10}

app = Dash(__name__, external_stylesheets=external_stylesheets)

# the dynamic div's children must be a list, so that it can be
# note that list += [newItem] is equivalent to list.append(newItem)

    #---------------------------------------
    # layout
    #---------------------------------------

app.layout=html.Div(
   id='output',
   children=[
      dcc.Store(id='memoryStore', storage_type='memory'),
      html.Button("See Storage",id='displayStorageButton', n_clicks=0),
      html.Button("Clear Messages",id='clearMessagesButton', n_clicks=0),
      dcc.Upload(
        id='uploaderWidget',
        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        multiple=False
        ),
      html.Div(id="messageDiv", children=[html.Span("")], style=dynamicDivStyle)
      ],
   )

    #---------------------------------------
    # uploaderWidget handler
    #---------------------------------------

@app.callback(
    Output('messageDiv',      'children', allow_duplicate=True),
    Output('memoryStore',     'data'),
    Input('uploaderWidget',   'filename'),
    State('messageDiv',       'children'),
    State('uploaderWidget',   'contents'),
    State('uploaderWidget',   'last_modified'),
    State('memoryStore',      'data'),
    prevent_initial_call=True)
def uploadHandler(filename, messageDivContents, contents, date, data):
    if filename == None:
        raise PreventUpdate
    print("--- 2: messageDiv before adding new info")
    messageDivContents += [html.P(filename)]
    messageDivContents += [html.P(len(contents))]
    data = data or {'ignore': 99}    # creates a default data dict if neede
    data['eaf'] = filename
    xmlUtils = XmlFileUtils(filename, "tmp", contents, verbose=True)
    localFile = xmlUtils.saveBytesToFile()
    data['localFile'] = localFile
    #result = xmlUtils.validElanXML()
    #data['valid'] = result['valid']
    formattedDate = datetime.datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')
    data['fileDate'] = formattedDate
    filesize = len(contents)/1000
    data['fileSize'] = "%sk" % filesize
    #pdb.set_trace()
    print(data)

    return messageDivContents, data

    #---------------------------------------
    # displayStorageButton handler
    #---------------------------------------

@app.callback(
    Output('messageDiv',          'children', allow_duplicate=True),
    Input('displayStorageButton', 'n_clicks'),
    State('messageDiv',           'children'),
    State('memoryStore',          'data'),
    prevent_initial_call=True)
def displayMemoryStore(buttonClicks, messageDivContents, data):
    if buttonClicks == 0:
        raise PreventUpdate
    el = html.Ul(id="list", children=[])
    for key in data.keys():
       el.children.append(html.Li("%s: %s" % (key, data[key])))
    messageDivContents += [el]
    return messageDivContents

    #---------------------------------------
    # clearMessagesButton handler
    #---------------------------------------

@app.callback(
    Output('messageDiv',          'children', allow_duplicate=True),
    Input('clearMessagesButton',  'n_clicks'),
    prevent_initial_call=True)
def clearMessages(buttonClicks):
    if buttonClicks == 0:
        raise PreventUpdate
    messageDivContents =  html.Div(id="messageDiv", children=[html.Span("")])
    return messageDivContents


if __name__ == '__main__':
    app.run(debug=True)
