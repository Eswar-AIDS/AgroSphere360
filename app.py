from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import time

# Define the data model for MQ-135
class GasData(BaseModel):
    sensor_id: str
    ammonia_voltage: float

app = FastAPI(title="MQ-135 Gas Sensor API")

# Initialize SQLite database
conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS gas_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id TEXT,
    ammonia_voltage REAL,
    timestamp REAL
)
""")
conn.commit()

# Root endpoint
@app.get("/")
def root():
    return {"status": "MQ-135 Gas Sensor API is running"}

# GET endpoint to retrieve latest data
@app.get("/data")
def get_data():
    cursor.execute("SELECT * FROM gas_data ORDER BY timestamp DESC LIMIT 10")
    rows = cursor.fetchall()
    result = [
        {
            "id": row[0],
            "sensor_id": row[1],
            "ammonia_voltage": row[2],
            "timestamp": row[3]
        } for row in rows
    ]
    return {"data": result}

# POST endpoint for ESP32
@app.post("/data")
def receive_data(data: GasData):
    cursor.execute(
        "INSERT INTO gas_data (sensor_id, ammonia_voltage, timestamp) VALUES (?, ?, ?)",
        (data.sensor_id, data.ammonia_voltage, time.time())
    )
    conn.commit()
    return {"status": "success"}

# Optional root endpoint for testing
@app.get("/")
def root():
    return {"message": "MQ-135 backend is live!"}
