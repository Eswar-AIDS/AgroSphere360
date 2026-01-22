from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(title="Agro IoT Backend")

# In-memory storage (for demo / prototype)
latest_data = {
    "gas": None,
    "temperature": None,
    "humidity": None,
    "timestamp": None
}

class SensorData(BaseModel):
    gas: float          # NH3 or Ethylene index
    temperature: float
    humidity: float

@app.get("/")
def root():
    return {"status": "Backend running"}

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "agro-backend"
    }

@app.post("/sensor-data")
def receive_sensor_data(data: SensorData):
    latest_data["gas"] = data.gas
    latest_data["temperature"] = data.temperature
    latest_data["humidity"] = data.humidity
    latest_data["timestamp"] = datetime.utcnow()

    return {"message": "Data received successfully"}

@app.get("/latest")
def get_latest_data():
    return latest_data
