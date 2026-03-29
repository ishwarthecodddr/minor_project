"""
FastAPI Backend for Telecom Customer Churn Prediction
A simple API that loads a pre-trained ML model and predicts customer churn.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np
from pathlib import Path
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Churn Prediction API")

# Enable CORS so frontend can communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for demo
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model from pickle file
MODEL_PATH = Path(__file__).resolve().parent / "churn_model.pkl"

with MODEL_PATH.open("rb") as f:
    model = pickle.load(f)


# Define the input data structure
class CustomerData(BaseModel):
    tenure: int           # How long the customer has been with the company
    MonthlyCharges: float # Monthly charges in dollars
    TotalCharges: float   # Total charges over the customer's tenure


# Root endpoint - just to check if API is running
@app.get("/")
def read_root():
    return {"message": "Churn Prediction API is running!"}


# Prediction endpoint
@app.post("/predict")
def predict_churn(data: CustomerData):
    """
    Predict whether a customer will churn based on their data.
    Returns: {"churn": "Yes"} or {"churn": "No"}
    """
    # Convert input data to numpy array for model
    features = np.array([[
        data.tenure,
        data.MonthlyCharges,
        data.TotalCharges
    ]])
    
    # Make prediction (0 = No churn, 1 = Churn)
    prediction = int(model.predict(features)[0])

    # Use probability when supported by model for better UX and risk bands
    if hasattr(model, "predict_proba"):
        churn_probability = float(model.predict_proba(features)[0][1])
    else:
        churn_probability = float(prediction)

    if churn_probability >= 0.65:
        risk_level = "HIGH"
        recommendation = "This customer is likely to leave soon. Offer a retention plan immediately."
    elif churn_probability >= 0.35:
        risk_level = "MEDIUM"
        recommendation = "This customer is at moderate risk. Proactive outreach could improve retention."
    else:
        risk_level = "LOW"
        recommendation = "This customer is likely to stay. Continue delivering consistent service quality."

    risk_factors = []
    if data.tenure <= 6:
        risk_factors.append("very short customer tenure")
    elif data.tenure >= 36:
        risk_factors.append("long customer relationship")

    if data.MonthlyCharges >= 85:
        risk_factors.append("high monthly bill")
    elif data.MonthlyCharges <= 35:
        risk_factors.append("low monthly bill")

    if data.TotalCharges <= 500:
        risk_factors.append("low cumulative spend")
    elif data.TotalCharges >= 2500:
        risk_factors.append("high cumulative spend")

    # Keep backward-compatible field while returning richer data for frontend
    churn_label = "Yes" if prediction == 1 else "No"
    return {
        "churn": churn_label,
        "risk_level": risk_level,
        "churn_probability": round(churn_probability, 4),
        "recommendation": recommendation,
        "risk_factors": risk_factors,
    }


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
