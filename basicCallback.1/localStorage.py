from dash import Dash, html, dcc, Output, Input, State, callback
from dash.exceptions import PreventUpdate

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Store(id='localStore', storage_type='local'),
    html.Table([
        html.Thead([
            html.Tr(html.Th('Click to store in:', colSpan="3")),
            html.Tr([
                html.Th(html.Button('localStorage', id='local-button')),
            ]),
            html.Tr([
                html.Th('Local clicks'),
            ])
        ]),
        html.Tbody([
            html.Tr([
                html.Td(0, id='local-clicks'),
            ])
        ])
    ])
])

    # add a click to the appropriate store.
@callback(Output('localStore', 'data'),
          Input('local-button', 'n_clicks'),
          State('localStore', 'data'))
def on_click(n_clicks, data):
    if n_clicks is None:
        # prevent the None callbacks is important with the store component.
        # you don't want to update the store for nothing.
        raise PreventUpdate

    # Give a default data dict with 0 clicks if there's no data.
    data = data or {'clicks': 0}

    data['clicks'] = data['clicks'] + 1
    return data

# output the stored clicks in the table cell.
@callback(Output('local-clicks', 'children'),
              # Since we use the data prop in an output,
              # we cannot get the initial data on load with the data prop.
              # To counter this, you can use the modified_timestamp
              # as Input and the data as State.
              # This limitation is due to the initial None callbacks
              # https://github.com/plotly/dash-renderer/pull/81
              Input('localStore', 'modified_timestamp'),
              State('localStore', 'data'))
def on_data(ts, data):
    if ts is None:
        raise PreventUpdate
    data = data or {}
    return data.get('clicks', 0)


if __name__ == '__main__':
    app.run(debug=True, port=8077, threaded=True)
