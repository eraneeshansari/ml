from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field
from sklearn.linear_model import LinearRegression

app = FastAPI()

# Training Data
X = [[500], [1000], [1500], [2000]]
y = [10, 20, 30, 40]

# Train Model
model = LinearRegression()
model.fit(X, y)

print("ML Model Training Completed!")

# User Input Schema
class HouseInput(BaseModel):
    size: float = Field(gt=0, le=100000)

# Browser UI
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("static/index.html")

# Prediction API
@app.post("/predict")
def predict(data: HouseInput):

    prediction = model.predict([[data.size]])

    return {
        "house_size": data.size,
        "predicted_price": round(float(prediction[0]), 2),
        "currency": "Lakh INR"
    }

