from fastapi import FastAPI
import numpy as np
import joblib
from pydantic import BaseModel

app  = FastAPI()
model = joblib.load("diabetes_model.pkl")

class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    BMI: float
    Age: int


@app.get("/")
def read_root():
       return {"message": "Diabetes Prediction API is live"}

@app.get("/predict")
def predict(data, response_model=DiabetesInput):
      input_data = np.array([[data.Pregnancies,data.Glucose,data.BloodPressure,data.BMI,data.Age]])
      prediction = model.predict(input_data)[0]
      return {"diabetic: ",bool(prediction)}