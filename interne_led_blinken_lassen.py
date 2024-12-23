from machine import Pin
import time

# Interne LED an Pin 2 (bei vielen ESP32-Boards)
led = Pin(2, Pin.OUT)

zahl = int(input(" Wie oft soll die interne blaue LED des ESP blinken?: "))


for i in range(zahl):
    led.value(1)  # LED an
    time.sleep(0.5)
    led.value(0)  # LED aus
    time.sleep(0.5)