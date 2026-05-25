# Environment Monitor

A Raspberry Pi 4 environmental monitoring system that continuously reads temperature, humidity, and air quality data from sensors and displays it on a live web dashboard.

## Hardware
- Raspberry Pi 4 Model B (4GB)
- DHT22 Temperature & Humidity Sensor
- MQ-135 Air Quality Sensor
- ADS1115 16-bit ADC (for analog MQ-135 signal)

## Software Stack
- Python 3 with Adafruit CircuitPython libraries
- SQLite for local data storage
- Flask REST API backend
- Chart.js frontend dashboard

## Features
- Live temperature, humidity, and air quality readings
- Historical data graphs with automatic 30-second refresh
- Data logged every 60 seconds to SQLite database
- Accessible from any device on the local network
- Runs automatically on boot via systemd services

## Wiring
- DHT22: VCC → Pin 1, DATA → Pin 7 (GPIO 4), GND → Pin 9
- ADS1115: VDD → Pin 17, GND → Pin 20, SCL → Pin 5, SDA → Pin 3
- MQ-135: VCC → Pin 2 (5V), GND → Pin 14, A0 → ADS1115 A0

## Setup
1. Flash Raspberry Pi OS (64-bit) to SD card
2. Enable I2C via raspi-config
3. Clone this repo and create a virtual environment
4. Install dependencies: `pip install flask adafruit-circuitpython-dht adafruit-circuitpython-ads1x15`
5. Enable systemd services for automatic startup

## Architecture
```
Sensors → GPIO/I2C → Python → SQLite → Flask API → Browser Dashboard
```
