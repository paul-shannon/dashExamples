from dash import Dash, dcc, html, Input, Output, callback, State
import json

app = Dash(__name__)

app.layout = html.Div([
    dcc.Store(id='dataStore', storage_type='session'),
    html.H4("Change the value in the text box to see callbacks in action"),
    html.Div([
        "Input: ",
        dcc.Input(id='inputWidget', value='', type='text')
    ]),
    html.Br(),
    html.Div([html.Span("Output: "),
              html.Span(id='outputWidget')
              ]),
    html.Div([html.Span("Upper case: "),
              html.Span(id='upperCaseOutputSpan')
              ]),
    html.Div(children=[html.Button("Save", id="saveButton"),
                       html.Button("Retrieve", id="retrieveButton")],
             style={"margin": 20}),
    html.Hr(),
    html.Div(id="storageView",
             style={"width": 300, "height": 300, "border": "1px;red;solid"}),
    html.Hr()
    ])


@callback(
    Output(component_id='outputWidget', component_property='children'),
    Input(component_id='inputWidget', component_property='value')
    )
def displayNewText(newText):
    return newText;

@callback(
    Output(component_id='upperCaseOutputSpan', component_property='children'),
    Input(component_id='inputWidget', component_property='value')
    #Input(component_id="saveButton", component_property="n_clicks")
    )
def displayNewText(newText):
     return newText.upper();
 
@callback(
    Output("dataStore", "data"),
    Input("saveButton", "n_clicks"),
    State("dataStore", 'data')
    )
def storeData(n_clicks, data):
    data = data or {'clicks': 0}
    data[0] = data[0] + n_clicks
    return data

@callback(
    Output("storageView", "children"),
    Input("dataStore", "data")
    )
def retrieveData(data):
    return data


# @callback(
#     Output(component_id="upperCaseOutputSpan", component_property="children"),
#     Input(component_id="saveButton", component_property="n_clicks")
#     )
# def displayNewText(newText):
#      print(ctx.triggered_id)
#      return newText.upper();
 
if __name__ == '__main__':
    app.run(debug=True)
