from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
import time

class GasData(BaseModel):
    sensor_id: str
    ammonia_voltage: float

app = FastAPI()
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

@app.post("/data")
def receive_data(data: GasData):
    cursor.execute(
        "INSERT INTO gas_data (sensor_id, ammonia_voltage, timestamp) VALUES (?, ?, ?)",
        (data.sensor_id, data.ammonia_voltage, time.time())
    )
    conn.commit()
    return {"status": "success"}
