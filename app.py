from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
import time

# Define data model from ESP32
class SensorData(BaseModel):
    temperature: float
    humidity: float
    sensor_id: str

app = FastAPI()

# Initialize SQLite (or change to Mongo/PostgreSQL later)
conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS sensor_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_id TEXT,
    temperature REAL,
    humidity REAL,
    timestamp REAL
)
""")
conn.commit()

@app.post("/data")
def receive_data(data: SensorData):
    cursor.execute(
        "INSERT INTO sensor_data (sensor_id, temperature, humidity, timestamp) VALUES (?, ?, ?, ?)",
        (data.sensor_id, data.temperature, data.humidity, time.time())
    )
    conn.commit()
    return {"status": "success"}
