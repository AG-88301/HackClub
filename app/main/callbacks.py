from main.__init__ import *

@app.callback(
    Output('graph', 'figure'),
    Input('memory', 'data'))
def updateGraph(mem):
    fig = go.Figure()
    for line in mem['lines']:
        fig.add_trace(line)
    return fig

@app.callback(
    [Output('memory', 'data'), Output('linesDiv', 'children')],
    Input('lineButton', 'n_clicks'),
    [State('memory', 'data'), State('linesDiv', 'children')],
    prevent_initial_call=True)
def addLine(n, mem, div):
    if n is None: raise PreventUpdate
    print(2)
    mem['n'] += 1
    mem['lines'].append(go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 2, 3, 4], mode='lines', name=f'Line {mem["n"]}'))
    div += [html.Div([
        html.Label(f"Line {mem['n']}"),
        dbc.Button('Delete', 
                   id={'type': 'deleteLineButton', 'index': mem["n"]}, 
                   className='deleteLineButton'),
        dcc.Dropdown(id={'type': 'lineDropdown', 'index': mem["n"]}, 
                     options=['Simple DT Model', 'Analytic DT Model']),
    ], className='lineWidgetDiv', id=f"{mem['n']}")]
    
    return mem, div

# @app.callback(
#     [Output('memory', 'data'), Output('linesDiv', 'children')], 
#     [Input({'type': 'deleteLineButton', 'index': ALL}, 'n_clicks')],
#     [State('memory', 'data'), State('linesDiv', 'children')],
#     prevent_initial_call=True)
# def deleteLine(n, mem, div):
#     if n is None: raise PreventUpdate
#     print(23)
#     ident = eval(dash.callback_context.triggered[0]['prop_id'].split('.')[0])['index']
#     for i in mem['lines']:
#         if i['name'] == f"Line {ident}":
#             mem['lines'].remove(i)
#             break
#     else: raise ValueError('Line not found')
    
#     for i in div:
#         if i['props']['children'][1]['props']['id']['index'] == ident:
#             div.remove(i)
#             break
#     else: raise ValueError("Not found")
    
#     return mem, div
