import dht
from machine import Pin
import time
import random

sensor = dht.DHT22(Pin(4))
print("timestamp,temperature,humidity")

counter = 0
base_temp = 24.0
base_hum  = 40.0

while True:
    sensor.measure()
    temp = base_temp + random.uniform(-2, 4)
    hum  = base_hum  + random.uniform(-5, 10)
    print(f"{counter},{temp:.1f},{hum:.1f}")
    counter += 1
    time.sleep(2)
