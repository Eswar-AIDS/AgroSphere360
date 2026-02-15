# 🌾 AgroSphere360

AgroSphere360 is a real-time environmental monitoring system built using ESP32 and MicroPython.  
The system collects temperature, humidity, and gas concentration data and displays it live on an OLED screen.

Designed for smart agriculture, greenhouse monitoring, and indoor air quality analysis.

---

## 📌 Project Overview

This project uses the ESP32 microcontroller running MicroPython firmware.  
Sensor data is processed locally and displayed via an OLED screen.

The system monitors:

- 🌡 Temperature (DHT22)
- 💧 Humidity (DHT22)
- 🌫 Gas Concentration / Air Quality (MQ-136)

The code was developed and uploaded using **Thonny IDE**.

---

## 🧰 Hardware Components

| Component | Purpose |
|------------|----------|
| ESP32 Dev Module | Main microcontroller |
| DHT22 | Temperature & humidity sensor |
| MQ-136 | Gas / air quality sensor |
| OLED Display (SSD1306) | Real-time data display |
| Breadboard & Jumper Wires | Circuit connections |

---

## 🛠 Software Stack

- MicroPython firmware (ESP32)
- Thonny IDE
- SSD1306 display driver
- DHT sensor driver

---

## 🔌 Pin Configuration (Example)

| Device | ESP32 Pin |
|--------|-----------|
| DHT22 Data | GPIO 4 |
| MQ-136 Analog | GPIO 34 (ADC) |
| OLED SDA | GPIO 21 |
| OLED SCL | GPIO 22 |
| VCC | 3.3V |
| GND | GND |

Adjust according to your wiring.

---

## 📂 Project Structure

AgroSphere360/
├── main.py
├── dht.py
├── ssd1306.py
└── README.md

---

## 🚀 Setup Instructions

### 1️⃣ Flash MicroPython Firmware

Download firmware from:
https://micropython.org/download/esp32/

Flash using esptool:

esptool.py --chip esp32 erase_flash
esptool.py --chip esp32 --baud 460800 write_flash -z 0x1000 firmware.bin


---

### 2️⃣ Connect Using Thonny

- Open Thonny
- Select Interpreter → MicroPython (ESP32)
- Select correct COM port
- Upload `main.py` to device

---

### 3️⃣ Run Program

The ESP32 will:

- Read DHT22 values
- Read MQ-136 analog values
- Display results on OLED
- Print debug output in Thonny shell

---

## 📊 Sample Output

OLED Display:

Temp: 28.4°C
Humidity: 61%
Gas Level: 185


---

## 🔬 Applications

- Smart agriculture monitoring
- Greenhouse environment control
- Indoor pollution monitoring
- IoT sensor data foundation

---

## 🔮 Future Enhancements

- WiFi-based cloud upload (MQTT)
- Real-time dashboard
- Alert system on threshold breach
- Mobile notification integration
- Data logging to SD card

---

## 👤 Author

Eswar B  
B.Tech – Artificial Intelligence & Data Science  

GitHub: https://github.com/Eswar-AIDS
