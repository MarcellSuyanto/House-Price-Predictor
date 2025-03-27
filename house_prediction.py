import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load dataset
teams = pd.read_csv("teams.csv")

# Select relevant columns
teams = teams[["team", "country", "year", "athletes", "age", "prev_medals", "medals"]]

# Display correlation matrix
correlation = teams[teams.columns[2:]].corr()["medals"]
print(correlation)

# Scatter plot: Athletes vs Medals
sns.lmplot(x="athletes", y="medals", data=teams, fit_reg=True, ci=None)
plt.title("Athletes vs Medals")
plt.show()

# Scatter plot: Age vs Medals
sns.lmplot(x="age", y="medals", data=teams, fit_reg=True, ci=None)
plt.title("Age vs Medals")
plt.show()

# Histogram of medals
teams["medals"].plot.hist()
plt.xlabel("Medals")
plt.ylabel("Frequency")
plt.title("Distribution of Medals")
plt.show()

# Check for missing values
missing_data = teams[teams.isnull().any(axis=1)]
print(missing_data)

# Drop rows with missing values
teams = teams.dropna()

# Split into training and testing sets
train = teams[teams["year"] < 2012].copy()
test = teams[teams["year"] >= 2012].copy()

# Train linear regression model
reg = LinearRegression()
predictors = ["athletes", "prev_medals"]
target = "medals"
reg.fit(train[predictors], train[target])

# Make predictions
predictions = reg.predict(test[predictors])
print(predictions)
