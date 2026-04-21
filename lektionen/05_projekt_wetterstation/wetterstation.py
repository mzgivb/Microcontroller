"""
Projekt 05: Wetterstation

LERNZIELE:
- DHT11 und OLED zusammen verwenden
- Werte formatiert anzeigen
- Fehlerbehandlung im Dauerbetrieb

VORAUSSETZUNG:
  lib/ssd1306.py ist auf den Pico kopiert (siehe SETUP.md).

HARDWARE:
  DHT11-Signal -> GPIO 13
  OLED SDA     -> GPIO 16
  OLED SCL     -> GPIO 17
  (Verkabelungsdetails siehe README.md dieses Projekts)
"""

from machine import Pin, I2C
import dht
import ssd1306
import time

# ----- Hardware initialisieren ----------------------------------------
sensor = dht.DHT11(Pin(13))
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)
display = ssd1306.SSD1306_I2C(128, 64, i2c)


# ----- Funktion: Werte auf das OLED bringen --------------------------
def zeige_werte(temp, hum):
    display.fill(0)

    display.text("WETTERSTATION", 12, 0)

    display.text("Temp: " + str(temp) + " C", 5, 20)
    display.text("Hum : " + str(hum)  + " %", 5, 35)

    # Trennlinie
    for x in range(10, 118, 3):
        display.pixel(x, 50, 1)

    display.text("Pico H", 36, 55)
    display.show()


# ----- Hauptschleife -------------------------------------------------
print("Wetterstation gestartet. Strg+C zum Beenden.")

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum  = sensor.humidity()
        zeige_werte(temp, hum)
        print("T:", temp, "°C   H:", hum, "%")
    except OSError as e:
        print("Sensorfehler:", e)
        display.fill(0)
        display.text("Sensor ?", 30, 25)
        display.show()
    time.sleep(3)
