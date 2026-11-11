
from sklearn.linear_model import LinearRegression

# Training Data
X = [[500], [1000], [1500], [2000]]
y = [10, 20, 30, 40]

# Create Model
model = LinearRegression()

# Train Model
model.fit(X, y)

print("ML Model Training Completed!")

# Prediction
size = [[2500]]
prediction = model.predict(size)

print("House Size:", size[0][0], "Sq.ft")
print("Predicted Price:", prediction[0], "Lakh")

