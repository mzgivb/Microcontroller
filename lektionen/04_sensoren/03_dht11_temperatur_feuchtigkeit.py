"""
Lektion 4.3: DHT11 -- Temperatur und Luftfeuchtigkeit

LERNZIELE:
- Einen digitalen Sensor über Bibliothek auslesen
- Fehler mit try/except abfangen

PYTHON-KONZEPTE:
- import dht
- try / except OSError

HARDWARE:
- DHT11 3-Pin-Modul (mit Widerstand auf der Platine)
- Signal -> GPIO 13 (Pin 17)
- VCC    -> 3V3 (Pin 36)
- GND    -> GND (Pin 38)

WICHTIG:
  - Nach jeder Messung mindestens 2 Sekunden warten -- sonst kommt ein Fehler!
  - dht ist ab Werk in MicroPython enthalten, keine extra Bibliothek nötig.
"""

from machine import Pin
import dht
from utime import sleep

sensor = dht.DHT11(Pin(13))

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum  = sensor.humidity()
        print("Temperatur:", temp, "°C   Feuchtigkeit:", hum, "%")
    except OSError as e:
        print("Sensor antwortet nicht:", e)
    sleep(3)


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Haucht den Sensor an -- beobachtet die Feuchtigkeit.
#
# 2. Gebt eine Warnung aus, wenn es "zu warm" (>27 °C) oder
#    "zu feucht" (>70 %) ist.
#
# 3. Kombiniert DHT11 mit der Melodie aus 3.3: ein Alarmton
#    erklingt, wenn die Werte Schwellen überschreiten.
#
# 4. CHALLENGE: Loggt alle 10 Sekunden die Werte in eine Liste
#    und gebt am Ende Min/Max/Mittelwert aus.
# ============================================================
