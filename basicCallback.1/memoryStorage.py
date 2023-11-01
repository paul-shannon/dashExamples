from dash import Dash, html, dcc, Output, Input, State, callback
from dash.exceptions import PreventUpdate
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Store(id='memoryStore', storage_type='memory'),
    html.Button('memoryStorage', id='memory-button'),
    html.Div(id="memory-clicks", children=0)
    ])

@callback(Output('memoryStore', 'data'),
          Input('memory-button', 'n_clicks'),
          State('memoryStore', 'data'))
def on_click(n_clicks, data):
  if n_clicks is None:
      raise PreventUpdate
  
  data = data or {'clicks': 0}    # Give a default data dict with 0 clicks if there's no data.
  data['clicks'] = data['clicks'] + 1
  return data

# output the stored clicks in the table cell.
@callback(Output('memory-clicks', 'children'),
              # Since we use the data prop in an output,
              # we cannot get the initial data on load with the data prop.
              # To counter this, you can use the modified_timestamp
              # as Input and the data as State.
              # This limitation is due to the initial None callbacks
              # https://github.com/plotly/dash-renderer/pull/81
              Input('memoryStore', 'modified_timestamp'),
              State('memoryStore', 'data'))
def on_data(ts, data):
    if ts is None:
        raise PreventUpdate
    data = data or {}
    return data.get('clicks', 0)


if __name__ == '__main__':
    app.run(debug=True, port=8077, threaded=True)