from dash import Dash, dcc, html, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    html.H4("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='', type='text')
    ]),
    html.Br(),
    html.Div([html.Span("Output: "),
              html.Span(id='my-output')
              ])
    ])


@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
    )
def displayNewText(newText):
    return newText;


if __name__ == '__main__':
    app.run(debug=True)
