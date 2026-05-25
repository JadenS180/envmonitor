import board
import adafruit_dht
import time

dht = adafruit_dht.DHT22(board.D4)

while True:
    try:
        temperature = dht.temperature * 9/5 + 32
        humidity = dht.humidity
        print(f"Temperature: {temperature:.1f}F  Humidity: {humidity:.1f}%")
    except RuntimeError as e:
        print(f"Reading error: {e}")
    time.sleep(2)
