from dash import Dash, dcc, html, Input, Output, callback, ctx

app = Dash(__name__)

app.layout = html.Div([
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
    html.Div(children=[html.Button("Save", id="saveButton")],
             style={"margin": 20})
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
     print(ctx.triggered_id)
     return newText.upper();
 
if __name__ == '__main__':
    app.run(debug=True)
