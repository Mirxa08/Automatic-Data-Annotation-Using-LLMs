import pandas as pd
import statsmodels.api as sm

# Read advertising data from CSV file
data = pd.read_csv('Advertising.csv')

# Define the independent variables (advertising channels)
X = data[['TV', 'radio', 'newspaper']]
# Define the dependent variable (sales)
y = data['sales']

# Add a constant term to the independent variables
X = sm.add_constant(X)

# Fit the multiple linear regression model
model = sm.OLS(y, X).fit()

# Extract the coefficients, t-stats, and p-values
coefficients = model.params
t_stats = model.tvalues
p_values = model.pvalues

# Predict sales based on the budget and coefficients
budget = 1000
predicted_sales = coefficients['const'] + coefficients['TV'] * budget + coefficients['radio'] * budget + coefficients['newspaper'] * budget
predicted_sales = round(predicted_sales, 2)

# Calculate R-squared
r_squared = model.rsquared
r_squared = round(r_squared, 2)

# Print the results
print("\nPredicted Sales with $1000 budget:", predicted_sales)
print("R-squared:", r_squared)
print("\nT-stats:")
print(t_stats)
print("\nP-values:")
print(p_values)
