from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import plotly.express as px

app = DjangoDash('Graph', external_stylesheets=[dbc.themes.CYBORG])
app.layout = html.Div([
    dcc.Store(id="memory", data={'n':0, 'lines':[]}), 
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
        ], style={'width':'50vw', 'padding':'2% 2% 2% 2%', 'background-color':'rgba(255,255,255,0.2)', 'margin':'2% 2% 2% 2%'}, id='rightDiv'),
    ], style={'display':'flex', 'flex-direction':'row'}),
    dbc.Button(id='newLineButton', children='+', style={'border-radius':'100%', 'height':'50px', 'width':'50px', 'position': 'fixed', 'top': '0', 'right': '0', 'z-index': '1000'}),
], id='main')

@app.callback(
    Output('graph', 'figure'),
    Input('memory', 'data'))
def updateGraph(mem):
    fig = go.Figure()
    for line in mem['lines']:
        fig.add_trace(line)
    return fig

@app.callback(
    Output('memory', 'data'),
    Input('lineButton', 'n_clicks'),
    State('memory', 'data'))
def addLine(n, mem):
    if n is None:
        raise PreventUpdate
    mem['n'] += 1
    mem['lines'].append(go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 2, 3, 4], mode='lines', name=f'Line {mem["n"]}'))
    return mem
