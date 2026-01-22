import urequests
import json
import time

ESP32_SENSOR_ID = "ESP32_01"
SERVER_URL = "https://agro-backend-env-8l1gqo9qj5.ap-south-1a.lb.nimbuz.tech/"  # Replace with deployed Nimbuz URL

def send_sensor_data(temp, hum):
    payload = {
        "sensor_id": ESP32_SENSOR_ID,
        "temperature": temp,
        "humidity": hum
    }
    headers = {"Content-Type": "application/json"}
    try:
        response = urequests.post(SERVER_URL, data=json.dumps(payload), headers=headers)
        print(response.text)
    except Exception as e:
        print("Error sending data:", e)

# Example loop
while True:
    temperature = 25.0  # Replace with actual sensor reading
    humidity = 60.0     # Replace with actual sensor reading
    send_sensor_data(temperature, humidity)
    time.sleep(10)      # send every 10 seconds
