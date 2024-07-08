import dash
from dash import dcc, html, Input, Output, State, ALL
import dash_bootstrap_components as dbc
from django_plotly_dash import DjangoDash
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate

app = DjangoDash('Graph', external_stylesheets=[dbc.themes.CYBORG, "/static/style.css", "/static/layout.css"])