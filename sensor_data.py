import sqlite3
import board
import busio
import adafruit_dht
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

# Initialize sensors
dht = adafruit_dht.DHT22(board.D4)
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
channel = AnalogIn(ads, 0)

# Initialize database
def init_db():
    conn = sqlite3.connect('envmonitor.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS readings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        temperature REAL,
        humidity REAL,
        air_quality REAL
    )''')
    conn.commit()
    conn.close()

# Save a reading to the database
def save_reading(temperature, humidity, air_quality):
    conn = sqlite3.connect('envmonitor.db')
    c = conn.cursor()
    c.execute('INSERT INTO readings (temperature, humidity, air_quality) VALUES (?, ?, ?)',
              (temperature, humidity, air_quality))
    conn.commit()
    conn.close()

# Main loop
init_db()
print("Starting data collection...")

while True:
    try:
        temperature = dht.temperature * 9/5 + 32
        humidity = dht.humidity
        air_quality = channel.voltage
        save_reading(temperature, humidity, air_quality)
        print(f"Saved - Temp: {temperature:.1f}F  Humidity: {humidity:.1f}%  Air Quality: {air_quality:.2f}V")
    except RuntimeError as e:
        print(f"Reading error: {e}")
    time.sleep(60)
