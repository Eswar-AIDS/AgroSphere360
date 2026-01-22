from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import time

class GasData(BaseModel):
    sensor_id: str
    ammonia_voltage: float

app = FastAPI(title="MQ-135 Gas Sensor API")

# Use a startup event to initialize DB safely
@app.on_event("startup")
def startup():
    global conn, cursor
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

@app.post("/sensor-data")
def receive_data(data: GasData):
    cursor.execute(
        "INSERT INTO gas_data (sensor_id, ammonia_voltage, timestamp) VALUES (?, ?, ?)",
        (data.sensor_id, data.ammonia_voltage, time.time())
    )
    conn.commit()
    return {"status": "success"}

@app.get("/")
def root():
    return {"message": "MQ-135 backend live!"}

@app.get("/latest")
def latest():
    cursor.execute("SELECT * FROM gas_data ORDER BY timestamp DESC LIMIT 1")
    row = cursor.fetchone()
    if row:
        return {"id": row[0], "sensor_id": row[1], "ammonia_voltage": row[2], "timestamp": row[3]}
    return {"message": "No data yet"}
