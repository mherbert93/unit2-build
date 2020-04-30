# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from datetime import datetime
import plotly.express as px

# Imports from this application
from app import app

from joblib import load
pipeline = load('assets/voting_model.joblib')

import pandas as pd

# data = {'Hotel stars': 5, 'Nr. rooms': 2959, 'Pool': 'YES', 'Gym': 'YES',
#                                          'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES', 'Free internet': 'YES'}

#hotels = pd.DataFrame(columns=['Hotel name', 'Hotel stars', 'Nr. rooms', 'Pool', 'Gym', 'Tennis court', 'Spa', 'Casino',
#                               'Free internet'], data=[['The Cosmopolitan Las Vegas'], [5], [2959], ['YES'],
#                                                       ['YES'], ['NO'], ['YES'],
#                                                       ['YES'], ['YES']])

#define hotel features here rather than have the user input them. Definately not prod ready/best practice to do it this way!
hotels = {'The Cosmopolitan Las Vegas': {'Hotel stars': 5, 'Nr. rooms': 2959, 'Pool': 'YES', 'Gym': 'YES',
                                         'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES', 'Free internet': 'YES'},

          'Paris Las Vegas': {'Hotel stars': 3, 'Nr. rooms': 2916, 'Pool': 'YES', 'Gym': 'YES',
                                         'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES', 'Free internet': 'YES'},

          'Tuscany Las Vegas Suites & Casino': {'Hotel stars': 1, 'Nr. rooms': 716, 'Pool': 'YES', 'Gym': 'YES',
                              'Tennis court': 'YES', 'Spa': 'YES', 'Casino': 'YES', 'Free internet': 'YES'},

          'Tropicana Las Vegas - A Double Tree by Hilton Hotel': {'Hotel stars': 3, 'Nr. rooms': 1467, 'Pool': 'YES', 'Gym': 'YES',
                                                'Tennis court': 'YES', 'Spa': 'YES', 'Casino': 'YES', 'Free internet': 'YES'},

          'The Westin las Vegas Hotel Casino & Spa': {'Hotel stars': 3, 'Nr. rooms': 826, 'Pool': 'YES', 'Gym': 'YES',
                                                'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES', 'Free internet': 'YES'},

          "Marriott's Grand Chateau": {'Hotel stars': 2, 'Nr. rooms': 732, 'Pool': 'YES', 'Gym': 'YES',
                                                      'Tennis court': 'NO', 'Spa': 'NO', 'Casino': 'NO',
                                                      'Free internet': 'YES'},

          "Hilton Grand Vacations on the Boulevard": {'Hotel stars': 2, 'Nr. rooms': 1228, 'Pool': 'YES', 'Gym': 'YES',
                                       'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES',
                                       'Free internet': 'YES'},

          "Monte Carlo Resort&Casino": {'Hotel stars': 3, 'Nr. rooms': 3003, 'Pool': 'YES', 'Gym': 'YES',
                                                      'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES',
                                                      'Free internet': 'NO'},

          "Wyndham Grand Desert": {'Hotel stars': 2, 'Nr. rooms': 787, 'Pool': 'YES', 'Gym': 'YES',
                                                      'Tennis court': 'YES', 'Spa': 'NO', 'Casino': 'NO',
                                                      'Free internet': 'YES'},

          "Caesars Palace": {'Hotel stars': 5, 'Nr. rooms': 3348, 'Pool': 'YES', 'Gym': 'YES',
                                   'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES',
                                   'Free internet': 'YES'},

          "Hilton Grand Vacations at the Flamingo": {'Hotel stars': 1, 'Nr. rooms': 315, 'Pool': 'YES', 'Gym': 'YES',
                                   'Tennis court': 'NO', 'Spa': 'NO', 'Casino': 'NO',
                                   'Free internet': 'YES'},

          "The Cromwell": {'Hotel stars': 4, 'Nr. rooms': 188, 'Pool': 'YES', 'Gym': 'NO',
                                   'Tennis court': 'NO', 'Spa': 'NO', 'Casino': 'YES',
                                   'Free internet': 'YES'},

          "Bellagio Las Vegas": {'Hotel stars': 5, 'Nr. rooms': 3933, 'Pool': 'YES', 'Gym': 'YES',
                           'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES',
                           'Free internet': 'YES'},

          "Wynn Las Vegas": {'Hotel stars': 5, 'Nr. rooms': 2700, 'Pool': 'YES', 'Gym': 'YES',
                           'Tennis court': 'YES', 'Spa': 'YES', 'Casino': 'YES',
                           'Free internet': 'YES'},

          "Encore at wynn Las Vegas": {'Hotel stars': 5, 'Nr. rooms': 2034, 'Pool': 'YES', 'Gym': 'YES',
                           'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES',
                           'Free internet': 'YES'},

          "The Venetian Las Vegas Hotel": {'Hotel stars': 5, 'Nr. rooms': 4027, 'Pool': 'YES', 'Gym': 'YES',
                             'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES',
                             'Free internet': 'YES'},

          "Excalibur Hotel & Casino": {'Hotel stars': 1, 'Nr. rooms': 3981, 'Pool': 'YES', 'Gym': 'YES',
                             'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES',
                             'Free internet': 'YES'},

          "Treasure Island- TI Hotel & Casino": {'Hotel stars': 3, 'Nr. rooms': 2884, 'Pool': 'YES', 'Gym': 'YES',
                             'Tennis court': 'YES', 'Spa': 'YES', 'Casino': 'YES',
                             'Free internet': 'YES'},

          "The Palazzo Resort Hotel Casino": {'Hotel stars': 5, 'Nr. rooms': 3025, 'Pool': 'YES', 'Gym': 'YES',
                             'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'YES',
                             'Free internet': 'YES'},

          "Trump International Hotel Las Vegas": {'Hotel stars': 5, 'Nr. rooms': 1282, 'Pool': 'YES', 'Gym': 'YES',
                                              'Tennis court': 'NO', 'Spa': 'YES', 'Casino': 'NO',
                                              'Free internet': 'YES'},

          "Circus Circus Hotel & Casino Las Vegas": {'Hotel stars': 1, 'Nr. rooms': 3773, 'Pool': 'NO', 'Gym': 'YES',
                                              'Tennis court': 'NO', 'Spa': 'NO', 'Casino': 'YES',
                                              'Free internet': 'YES'}
          }


dcc.Input(
    id='hotels_dictionary',
    placeholder='Enter a value...',
    type='number',
    value=''
)

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'),
        dcc.Markdown('#### Which hotel would you be staying at?'),
        dcc.Dropdown(
            id='hotel_name',
            options=[
                {'label': 'The Cosmopolitan Las Vegas', 'value': 'The Cosmopolitan Las Vegas'},
                {'label': 'Paris Las Vegas', 'value': 'Paris Las Vegas'},
                {'label': 'Tuscany Las Vegas Suites & Casino', 'value': 'Tuscany Las Vegas Suites & Casino'},
                {'label': 'Tropicana Las Vegas - A Double Tree by Hilton Hotel',
                 'value': 'Tropicana Las Vegas - A Double Tree by Hilton Hotel'},
                {'label': 'Hilton Grand Vacations on the Boulevard',
                 'value': 'Hilton Grand Vacations on the Boulevard'},
                {'label': 'The Westin las Vegas Hotel Casino & Spa',
                 'value': 'The Westin las Vegas Hotel Casino & Spa'},
                {'label': "Marriott's Grand Chateau", 'value': "Marriott's Grand Chateau"},
                {'label': "Wyndham Grand Desert", 'value': "Wyndham Grand Desert"},
                {'label': "Monte Carlo Resort&Casino", 'value': "Monte Carlo Resort&Casino"},
                {'label': "Caesars Palace", 'value': "Caesars Palace"},
                {'label': "The Cromwell", 'value': "The Cromwell"},
                {'label': "Hilton Grand Vacations at the Flamingo", 'value': "Hilton Grand Vacations at the Flamingo"},
                {'label': "Wynn Las Vegas", 'value': "Wynn Las Vegas"},
                {'label': "Encore at wynn Las Vegas", 'value': "Encore at wynn Las Vegas"},
                {'label': "The Venetian Las Vegas Hotel", 'value': "The Venetian Las Vegas Hotel"},
                {'label': "Bellagio Las Vegas", 'value': "Bellagio Las Vegas"},
                {'label': "Trump International Hotel Las Vegas", 'value': "Trump International Hotel Las Vegas"},
                {'label': "The Palazzo Resort Hotel Casino", 'value': "The Palazzo Resort Hotel Casino"},
                {'label': "Excalibur Hotel & Casino", 'value': "Excalibur Hotel & Casino"},
                {'label': "Treasure Island- TI Hotel & Casino", 'value': "Treasure Island- TI Hotel & Casino"},
                {'label': "Circus Circus Hotel & Casino Las Vegas", 'value': "Circus Circus Hotel & Casino Las Vegas"},
            ],
            value='The Cosmopolitan Las Vegas',
            className='mb-10',
        ),
        dcc.Markdown('#### How many total reviews have you left on Tripadvisor?'),
        dcc.Input(
            id='total_reviews',
            placeholder='Enter a value...',
            type='number',
            value=1,
            min=1
        ),
        dcc.Markdown('#### How many hotel reviews have you left on Tripadvisor?'),
        dcc.Input(
            id='total_hotel_reviews',
            placeholder='Enter a value...',
            type='number',
            value=1,
            min=1
        ),
        dcc.Markdown('#### How many helpful votes have you left on Tripadvisor?'),
        dcc.Input(
            id='helpful_votes',
            placeholder='Enter a value...',
            type='number',
            value=0,
            min=0
        ),
        dcc.Markdown('#### Which continent are you located on?'),
        dcc.Dropdown(
            id='continent',
            options=[
                {'label': 'North America', 'value': 'North America'},
                {'label': 'Europe', 'value': 'Europe'},
                {'label': 'Oceania', 'value': 'Oceania'},
                {'label': 'Asia', 'value': 'Asia'},
                {'label': 'South America', 'value': 'South America'},
                {'label': 'Africa', 'value': 'Africa'},
            ],
            value='North America',
            className='mb-3',
        ),
        dcc.Markdown('#### What country are you from?'),
        dcc.Dropdown(
            id='country',
            options = [
                {'label': 'United States', 'value': 'USA'},
                {'label': 'Canada', 'value': 'Canada'},
                {'label': 'United Kingdom', 'value': 'UK'},
                {'label': 'Other', 'value': 'Other'},
            ],
            value = 'USA',
            className='mb-3',
        ),
        dcc.Markdown('#### Which quarter of the year would you be staying?'),
        dcc.Dropdown(
            id='quarter',
            options=[
                {'label': 'Dec-Feb', 'value': 'Dec-Feb'},
                {'label': 'Mar-May', 'value': 'Mar-May'},
                {'label': 'Jun-Aug', 'value': 'Jun-Aug'},
                {'label': 'Sep-Nov', 'value': 'Sep-Nov'},
            ],
            value='Dec-Feb',
            className='mb-3',
        ),
        dcc.Markdown('#### What type of traveler are you?'),
        dcc.Dropdown(
            id='traveler_type',
            options=[
                {'label': 'Couples', 'value': 'Couples'},
                {'label': 'Families', 'value': 'Families'},
                {'label': 'Business', 'value': 'Business'},
                {'label': 'Friends', 'value': 'Friends'},
                {'label': 'Solo', 'value': 'Solo'},
            ],
            value='Couples',
            className='mb-3',
        ),
        dcc.Markdown('#### What month would you be leaving your review?'),
        dcc.Dropdown(
            id='month',
            options=[
                {'label': 'January', 'value': 'January'},
                {'label': 'February', 'value': 'February'},
                {'label': 'March', 'value': 'March'},
                {'label': 'April', 'value': 'April'},
                {'label': 'May', 'value': 'May'},
                {'label': 'June', 'value': 'June'},
                {'label': 'July', 'value': 'July'},
                {'label': 'August', 'value': 'August'},
                {'label': 'September', 'value': 'September'},
                {'label': 'October', 'value': 'October'},
                {'label': 'November', 'value': 'November'},
                {'label': 'December', 'value': 'December'},
            ],
            value=datetime.now().strftime("%B"), #Get current month name
            className='mb-3',
        ),
        dcc.Markdown('#### What day of the week would you be leaving your review?'),
        dcc.Dropdown(
            id='day',
            options=[
                {'label': 'Sunday', 'value': 'Sunday'},
                {'label': 'Monday', 'value': 'Monday'},
                {'label': 'Tuesday', 'value': 'Tuesday'},
                {'label': 'Wednesday', 'value': 'Wednesday'},
                {'label': 'Thursday', 'value': 'Thursday'},
                {'label': 'Friday', 'value': 'Friday'},
                {'label': 'Saturday', 'value': 'Saturday'},
            ],
            value=datetime.now().strftime("%A"),  # Get current day name
            className='mb-3',
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2(id='selected_hotel', className='mb-5'),
        html.Div(id='prediction-content', className='lead', style={'textAlign': 'center', 'fontSize': 80}),
        html.Div(id='pred_graph'),
    ],
)

layout = dbc.Row([column1, column2])


@app.callback(
    [Output('prediction-content', 'children'),
     Output('selected_hotel', 'children'),
     Output('pred_graph', 'children')],
    [Input('total_reviews', 'value'), Input('total_hotel_reviews', 'value'), Input('helpful_votes', 'value'),
     Input('country', 'value'), Input('quarter', 'value'), Input('traveler_type', 'value'), Input('hotel_name', 'value'),
     Input('continent', 'value'), Input('month', 'value'), Input('day', 'value')],
)

def predict(total_reviews, total_hotel_reviews, helpful_votes, country, quarter, traveler_type, hotel_name, continent,
            month, day):
    df = pd.DataFrame(
        columns=['Nr. reviews', 'Nr. hotel reviews', 'Helpful votes', 'Hotel stars', 'Nr. rooms', 'User country',
                 'Period of stay', 'Traveler type', 'Pool', 'Gym', 'Tennis court', 'Spa', 'Casino', 'Free internet',
                 'Hotel name', 'User continent', 'Review month', 'Review weekday'],
        # data=[[total_reviews, total_hotel_reviews, helpful_votes, hotels.loc[hotel_name, 'Hotel stars'], hotels.loc[hotel_name, 'Nr. rooms'],
        #        country, quarter, traveler_type, hotels.loc[hotel_name, 'Pool'], hotels.loc[hotel_name, 'Gym'],
        #       hotels.loc[hotel_name, 'Tennis court'], hotels.loc[hotel_name, 'Spa'], hotels.loc[hotel_name, 'Casino'],
        #       hotels.loc[hotel_name, 'Free internet'], hotel_name, continent, month, day]]
        data=[[total_reviews, total_hotel_reviews, helpful_votes, hotels[hotel_name]['Hotel stars'],
               hotels[hotel_name]['Nr. rooms'],
               country, quarter, traveler_type, hotels[hotel_name]['Pool'], hotels[hotel_name]['Gym'],
              hotels[hotel_name]['Tennis court'], hotels[hotel_name]['Spa'], hotels[hotel_name]['Casino'],
              hotels[hotel_name]['Free internet'], hotel_name, continent, month, day]]

    )
    y_pred = pipeline.predict(df)[0]
    y_prob_pred = pipeline.predict_proba(df)[0]

    df_prob = pd.DataFrame({'Classes': ['Bad', 'Average', 'Excellent'], 'Probabilities': [y_prob_pred[1], y_prob_pred[0],
                                                                                          y_prob_pred[2]]})

    hotel_text = "Your rating of " + hotel_name

    return y_pred, hotel_text, html.Div(
            dcc.Graph(
                id='bar chart',
                figure={
                    "data": [
                        {
                            "x": df_prob['Classes'],
                            "y": df_prob['Probabilities'],
                            "type": "bar",
                        }
                    ],
                    "layout": {
                        'title': 'Probability Distribution',
                        "xaxis": {"title": "Ratings"},
                        "yaxis": {"title": "Probability"}
                    },
                },
            )
    )
