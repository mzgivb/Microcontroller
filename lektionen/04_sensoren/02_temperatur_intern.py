"""
Lektion 4.2: Interner Temperatursensor des Pico

LERNZIELE:
- Der Pico hat einen eingebauten Temperatursensor -- wie geht das?
- Rohwerte über Physik in Grad Celsius umrechnen

PYTHON-KONZEPTE:
- ADC(4) ist der interne Sensor
- Formel: Temperatur = 27 - (Spannung - 0,706) / 0,001721

HARDWARE:
- Nur der Pico, nichts extern.
"""

from machine import ADC
from utime import sleep

sensor = ADC(4)            # Kanal 4 = interner Temperatursensor
faktor = 3.3 / 65535       # Rohwert -> Spannung in Volt

while True:
    roh = sensor.read_u16()
    spannung = roh * faktor
    temp_c = 27 - (spannung - 0.706) / 0.001721
    print("Rohwert:", roh,
          "  Spannung:", round(spannung, 3), "V",
          "  Temperatur:", round(temp_c, 1), "°C")
    sleep(1)


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Haltet den Pico in der Hand -- die Temperatur steigt.
#    Warum? Ist das ein brauchbares Außenthermometer?
#
# 2. Gebt die Temperatur nur aus, wenn sie sich um mindestens
#    0,5 °C vom letzten Wert unterscheidet.
#
# 3. Zeigt die Temperatur auf dem OLED an (Kombi mit 3.2).
# ============================================================
