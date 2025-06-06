from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Define the input data model
class RideFeatures(BaseModel):
    distance: float
    day: int
    hour: int
    temp: float
    clouds: float
    pressure: float
    humidity: float
    wind: float
    rain: float

app = FastAPI(title="Surge Pricing API")

# Load the model and label encoder (no scaler now)
model = joblib.load("model/random_forest_model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")

@app.post("/predict")
def predict(features: RideFeatures):
    # Convert input features to numpy array
    X = np.array([[ 
        features.distance,
        features.day,
        features.hour,
        features.temp,
        features.clouds,
        features.pressure,
        features.humidity,
        features.wind,
        features.rain
    ]])


    pred_encoded = model.predict(X)

    # Decode prediction
    pred_surge = label_encoder.inverse_transform(pred_encoded)[0]

    return {"predicted_surge_multiplier": float(pred_surge)}
