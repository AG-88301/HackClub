from dash import dcc, html, Input, Output
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go
import plotly.express as px

app = DjangoDash('Graph')
app.layout = html.Div([dcc.Graph(id='graph'), dcc.Input(id="inp")], style={'height':'70vh'})

@app.callback(
    Output('graph', 'figure'),
    Input('inp', 'value')
)
def update_figure(inp):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1,2,3], y=[5,3,6], mode='lines'))
    fig.add_trace(go.Scatter(x=[14,23,45], y=[3,4,9], mode='lines'))
    return fig
