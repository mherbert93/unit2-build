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
        
            The dataset I selected was obtained from the UCI machine learning repository. It is compromised of just over 
            500 TripAdvisor reviews of 21 different hotels on the Las Vegas strip. This app uses 3 different models, 
            combined into a voting ensemble via sklearn's votingclassifier. It comprises of a random forest, xgboost, 
            and logistic regression model. The voting classifier uses a soft voting option which predicts the class 
            label based on the argmax of the sums of the predicted probabilities. It is also weighted 2(random forest), 
            1(logistic regression), and 2(xgboost). The reason for this being my logistic regression model overall 
            performs worse than the other two, but also is stronger in some areas so it is worth keeping in our ensemble.

            """
            
            """
            ## Preprocessing
            
            Because of the limited data size and extreme class imbalance, the first bit of processing that had to be 
            done was to group our ratings. In the dataset they are a rating 1-5. I turn these 5 classes into 3: 
            Bad(rating of 1-2), Average(rating of 3-4), and Excellent(rating of 5). This allowed me to have a larger 
            samplesize of the minority class to train on.
             
            Besides that, I also am grouping the country of the reviewer into "USA", "Canada", "UK", and "Other". Some 
            data on the properties was also not correct. There were multiple hotels flagged as having a casino that do 
            not have a casino and so I changed these as well. Because of the extreme class imbalance I occurred(8% of 
            reviews were bad, which was only 33 observations! Not much data to work with here), I had to treat this data 
            in some way. I decided to randomly oversample all but the majority class.  
            
            For the random forest and xgboost models, I used an ordinal encoder prior to fitting the model. For the
            logistic regression model, I applied one hot encoding, followed by a standard scalar and then selectkbest
            to determine the optimal number of features.
            """
            
            """
            ## Performance of the model
            
            The baseline accuracy for my model is 46.5% on the test dataset. This is the accuracy I would get if I 
            chose the majority class each time. Our model is able to achieve 56.4% accuracy on the test dataset. However,
            accuracy does not tell the whole story because of the imbalanced classes. Instead, accuracy measures like precision,
            recall, and roc auc are more applicable here. 
            """
        ),
        html.Img(src='assets/accuracy.PNG', className='img-fluid'),
        dcc.Markdown(

            """
            Overall, considering the tiny dataset(~500 observations), and imbalanced classes, I am satisfied with
            the model results. The model beats the baseline, while still also being able to correctly classify some of
            the minority class. For this app to be useful for real world use, I believe that it would need more data. It
            would need a larger sample size and more predictive features. 
            """
        )

    ],
)

layout = dbc.Row([column1])