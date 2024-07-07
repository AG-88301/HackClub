from dash import dcc, html, Input, Output, State, MATCH, ALL
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate

app = DjangoDash('Graph', external_stylesheets=[dbc.themes.CYBORG, "/static/style.css"])
app.layout = html.Div([
    dcc.Store(id="memory", data={'n':1,'lines':[go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 2, 3, 4], mode='lines', name='Line 1')]}), 
    dbc.Popover(
        dbc.ListGroup([
                dbc.Button('Line', id='lineButton', style={'margin':f'{(p:=5)}% 0% {p}% 0%'}),
                dbc.Button('Bounding Line', id='boundingButton', style={'margin':f'{p}% 0% {p}% 0%'}),
                dbc.Button('Min/Max Line', id='minMaxButton', style={'margin':f'{p}% 0% {p}% 0%'})
            ],
            className="p",
        ),
        target="newLineButton",
        body=True,
        trigger="hover",
    ),
    html.Div([
        html.Div([
            dcc.Graph(id='graph'), 
        ], style={'width':'47vw', 'margin':'2% 2% 2% 2%'}),
        html.Div([
            html.Label('X:', id='xLabel'),
            html.Div([html.Div([
                html.Label(f"Line 1"),
                dbc.Button('Delete', id={'type': 'deleteLineButton', 'index': 1}, style={'margin':'0% 0% 0% 2%'}),
                dcc.Dropdown(id={'type': 'lineDropdown', 'index': 1}, options=['Simple DT Model', 'Analytic DT Model']),
            ], style={'margin':'2% 0% 2% 0%'}, id='1')], id='linesDiv', style={'display':'flex', 'flex-direction':'column'}),
        ], style={'width':'50vw', 'padding':'2% 2% 2% 2%', 'background-color':'rgba(255,255,255,0.2)', 'margin':'2% 2% 2% 2%'}, id='rightDiv'),
    ], style={'display':'flex', 'flex-direction':'row', 'overflow':'auto'}),
    dbc.Button(id='newLineButton', children='+', style={'border-radius':'100%', 'height':'50px', 'width':'50px', 'position': 'fixed', 'top': '0', 'right': '0', 'z-index': '1000'}),
], id='main', style={'width':'100vw', 'background-color':'rgba(0,0,0,0)'})

@app.callback(
    Output('graph', 'figure'),
    Input('memory', 'data'))
def updateGraph(mem):
    fig = go.Figure()
    for line in mem['lines']:
        fig.add_trace(line)
    return fig

# @app.callback(
#     [Output('memory', 'data'), Output('linesDiv', 'children')],
#     Input('lineButton', 'n_clicks'),
#     [State('memory', 'data'), State('linesDiv', 'children')])
# def addLine(n, mem, div):
#     print(2)
#     if n is None:
#         raise PreventUpdate
#     mem['n'] += 1
#     mem['lines'].append(go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 2, 3, 4], mode='lines', name=f'Line {mem["n"]}'))
#     div += [html.Div([
#         html.Label(f"Line {mem['n']}"),
#         dbc.Button('Delete', id={'type': 'deleteLineButton', 'index': mem["n"]}, style={'margin':'0% 0% 0% 2%'}),
#         dcc.Dropdown(id={'type': 'lineDropdown', 'index': mem["n"]}, options=['Simple DT Model', 'Analytic DT Model']),
#     ], style={'margin':'2% 0% 2% 0%'})]
    
#     return mem, div

@app.callback(
    [Output('memory', 'data'), Output('linesDiv', 'children')], 
    [Input({'type': 'deleteLineButton', 'index': MATCH}, 'n_clicks')],
    [State('memory', 'data'), State('linesDiv', 'children'), State({'type': 'deleteLineButton', 'index': MATCH}, 'id')])
def deleteLine(n, mem, div, ident):
    print(23)
    if n is None: raise PreventUpdate
    for i in mem['lines']:
        if i['name'] == f"Line {ident['index']}":
            mem['lines'].remove(i)
            break
    else: raise ValueError('Line not found')
    
    for i in div:
        if i['props']['children'][1]['props']['id']['index'] == ident['index']:
            div.remove(i)
            print(i)
            break
    else: raise ValueError("Not found")
    
    return mem, div
