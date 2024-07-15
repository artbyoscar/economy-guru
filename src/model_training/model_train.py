from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Prepare data
X = df[['unemployment_rate']]
y = df['gdp_growth']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)
print(predictions)
