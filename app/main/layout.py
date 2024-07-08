from main.callbacks import *
from main.__init__ import *

app.layout = html.Div([
    # temporary for deleteLine testing
    dcc.Store(id="memory", data={'n':1,'lines':[go.Scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 2, 3, 4], mode='lines', name='Line 1')]}), 
    # end temp section
    
    # dcc.Store(id="memory", data={'n':0,'lines':[]}), 
    dbc.Popover(
        dbc.ListGroup([
                dbc.Button('Line', id='lineButton'),
                dbc.Button('Bounding Line', id='boundingButton'),
                dbc.Button('Min/Max Line', id='minMaxButton')
            ],
        ),
        target="newLineButton",
        body=True,
        trigger="hover",
    ),
    html.Div([
        html.Div([
            html.H1('Graph'),
            dcc.Graph(id='graph'), 
        ], id='leftDiv'),
        html.Div([
            html.Label('X:', id='xLabel'),
            html.Div([
                
                # temporary for deleteLine testing
                html.Div([
                    html.Label(f"Line 1"),
                    dbc.Button('Delete', 
                               id={'type': 'deleteLineButton', 'index': 1}, 
                               className='deleteLineButton'),
                    dcc.Dropdown(id={'type': 'lineDropdown', 'index': 1}, 
                                 options=['Simple DT Model', 'Analytic DT Model']),
                ], className='lineWidgetDiv', id='1')
                # end temp section
                
            ], id='linesDiv'),
        ], id='rightDiv'),
    ], id='mainBody'),
    dbc.Button(id='newLineButton', children='+'),
], id='main')
