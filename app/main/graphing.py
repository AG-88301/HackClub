from dash import dcc, html, Input, Output, State
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import plotly.express as px

app = DjangoDash('Graph')
app.layout = html.Div([
    dcc.Store(id="memory", data={'n':0, 'lines':[]}), 
    html.Div([
        html.Div([
            dcc.Graph(id='graph'), 
        ], style={'width':'45vw'}),
        html.Div([
            html.Label('X:')
        ], style={'width':'45vw', 'padding':'2% 2% 2% 2%'}),
    ], style={'display':'flex', 'flex-direction':'row'}),
    html.Button(id='newLineButton', children='+')
])

@app.callback(
    Output('graph', 'figure'),
    Input('memory', 'data')
)
def update_figure(inp):
    fig = go.Figure()
    for line in inp['lines']:
        fig.add_trace(line)
    return fig

@app.callback(
    Output('memory', 'data'),
    Input('newLineButton', 'n_clicks'),
    State('memory', 'data')
)
def upd(n_clicks, mem):
    if n_clicks is None: raise PreventUpdate
    mem['n'] += 1
    mem['lines'].append(go.Scatter(x=[mem['n']*1,2,3], y=[5,3,6], mode='lines'))
    return mem