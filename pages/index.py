# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## How are you likely to rate a hotel, based on your tripadvisor stats.

            Have you ever been on TripAdvisor, looking at hotels you've never been to before and trying to decide whether 
            to give them a try? The idea behind this app is to help users get a better idea of whether they would like 
            a particular hotel. 

            """
        ),
        dcc.Link(dbc.Button('Make some predictions', color='primary'), href='/predictions')
    ],
    md=4,
)

# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)
#
# column2 = dbc.Col(
#     [
#         dcc.Graph(figure=fig),
#     ]
# )

layout = dbc.Row([column1])