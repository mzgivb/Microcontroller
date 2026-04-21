from machine import Pin
import time

led = Pin(2, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_UP)

while True:
    if button.value() == 0:  # Taster gedrückt
        led.value(1)
    else:
        led.value(0)
    time.sleep(0.1)