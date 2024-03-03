import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('Advertising.csv')

# Define the target variable (sales)
y = data['sales']

# Define the budget
budget = 1000

# Define the sales target
target_sales = 300


def linear_regression(ad_channel):
    # Selecting only specified advertising channel for linear regression
    X = data[[ad_channel]]

    # Fit the model
    model = LinearRegression()
    model.fit(X, y)

    # Predict sales for $1000 advertising budget on specified channel
    predicted_sales = model.predict([[budget]])[0]

    # Plotting the data and regression line
    plt.scatter(X, y, color='blue', label='Actual Sales')
    plt.plot(X, model.predict(X), color='red', label='Regression Line')
    plt.axhline(y=predicted_sales, color='green', linestyle='--',
                label='Predicted Sales: {:.2f}'.format(predicted_sales))
    plt.xlabel('Advertising Budget ($)')
    plt.ylabel('Sales (units)')
    plt.title('Linear Regression: {} vs Sales'.format(ad_channel))
    plt.legend()
    plt.grid(True)
    plt.show()

    # R-squared
    r_squared = r2_score(y, model.predict(X))

    # T-stat and p-value
    X_with_const = sm.add_constant(X)  # Adding constant term for statsmodels
    est = sm.OLS(y, X_with_const).fit()
    t_stat = est.tvalues[1]
    p_value = est.pvalues[1]

    print("\nResults", ad_channel.capitalize(), "Channel:")
    print("Predicted Sales for $1000", ad_channel, " and Advertising Budget: {:.2f}".format(predicted_sales))
    print("R^2: {:.2f}".format(r_squared))
    print("T-stat: {:.2f}".format(t_stat))
    print("P-val: {:.2f}".format(p_value))


# Perform linear regression for each advertising channel and plot the results
for channel in ['TV', 'radio', 'newspaper']:
    linear_regression(channel)
