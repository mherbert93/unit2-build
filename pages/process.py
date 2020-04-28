# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(

            """
        
            ## Dataset and model selection
        
            The dataset that I selected was obtained from the UCI machine learning repository. It consist of just over 500
            Tripadvisor reviews of 21 different hotels located on the Las Vegas strip. This app uses 3 different models, 
            combined into a voting ensemble via sklearn's votingclassifier. It is comprised of a random forest, xgboost, 
            and logistic regression model. The voting classifier uses a soft voting option which predicts the class label 
            based on the argmax of the sums of the predicted probabilities. 

            """
            
            """
            ## Preprocessing
            
            Due to the limited data size and extreme class imbalance, the first bit of processing that had to be done was
            to group our ratings. In the dataset they are a rating 1-5. I decide to turn these 5 classes into 3:
            Bad(rating of 1-2), Average(rating of 3-4), and Excellent(rating of 5). This allowed me to have a larger
            samplesize of the minority class to train on.
             
            In addition to that, I also am grouping the country of the reviewer into "USA", "Canada", "UK", and "Other".
            Some of the data on the properties was also not correct. There were multiple hotels flagged as having a casino
            that actually do not have a casino and so I changed these as well.
            """
        )
    ],
)

layout = dbc.Row([column1])