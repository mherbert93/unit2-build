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
            ## Insights
            
            Looking under the hood, there are some interesting insights we can gather from the model.
            
            Lets first look at the permutation importances of our 3 models. The permutation importance is a great 
            way to see which features have the largest effect on the performance of your model.
            """
        ),
        html.Img(src='assets/xgboost_permutation.PNG', className='img-fluid', title='XGboost'),
        html.Img(src='assets/forest_permutation.PNG', className='img-fluid', title='Random Forest'),
        html.Img(src='assets/logistic_permutation.PNG', className='img-fluid', title='Logistic Regression'),
        dcc.Markdown(
            """
                            XGboost                             Random Forest                        Logistic Regression
            
            
            """
            """
            The permutation importances for these models were calculated with roc auc as the scoring metric. We can gain
            some interesting insights from this.

            Starting from the left is our xgboost model. The first thing that stuck out to me is how the number of hotel
            reviews that the user has left on Tripadvisor was the most predictive feature. This shows that more active 
            TripAdvisor users may vote differently than less frequent ones. The second most predictive feature is the 
            specific hotel. This is not too surprising, as better hotels generally will have less negative reviews.

            The model in the middle is our random forest model. Our most predictive feature here is the total number of 
            reviews that the user has left on Tripadvisor. If you really think about it though, it makes sense. A user 
            that has only left 1 review means they opened their account to make this particular review. This could be 
            because they had a terrible experience, but also because they had a great experience. Not surprisingly 
            however is that the particular hotel and how many stars that hotel has are also very predictive features. 
            Certain hotels are much more likely to have positive reviews than negative, and vice versa.

            Finally we have our logistic regression model. The features here are one hot encoded, so they look different
            from the other two models. Again here we can see the number of hotel reviews is the top predictive feature.

            While all the models generally find the same features important, there is some variation. That, combined with
            the small sample size to train on, is what drove my decision to use a voting ensemble. I believe a voting 
            ensemble allows the model to generalize better and perform more consistently vs using any one specific model.
            """
        ),
        html.Img(src='assets/pdp_hotel_stars.PNG', className='img-fluid', title='PDP'),
        dcc.Markdown(
            """
            Now this I find interesting. Class 0 corresponds to "Average", class 1 is "Bad", and class 2 is "Excellent". 
            From the PDP we can see that as hotel stars goes up, there is a larger impact on whether it is classified as 
            average or excellent. The interesting part though is that it has almost no effect on bad ratings. To me this 
            says that if someone will rate a hotel badly, it has less to do with the class of the property and more to 
            do with other factors. Number of reviews, perhaps?
            """
        ),
        html.Img(src='assets/pdp_interact.PNG', className='img-fluid', title='PDP Interact'),
        dcc.Markdown(
            """
            When adding in total reviews to our plot, it becomes much clearer that users who have only left 1 review
            is a significant portion of the probability of predicting the class. You can see that as hotel stars goes up,
            the probability does not change much. But as reviews goes up, it significantly changes the probability. 
            """
        )

    ],
)
column2 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## test

            test
            """
        ),

    ],
)

layout = dbc.Row([column1])