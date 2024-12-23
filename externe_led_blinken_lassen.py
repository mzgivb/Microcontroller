from machine import Pin
from utime import sleep

led = Pin(8, Pin.OUT)



while True:
   led.value(1)  # LED einschalten
   sleep(0.5)      # 1 Sekunde warten
   led.value(0)  # LED ausschalten
   sleep(0.5)      # 1 Sekunde warten