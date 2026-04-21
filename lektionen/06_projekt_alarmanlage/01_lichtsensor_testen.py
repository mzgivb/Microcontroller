"""
Projekt 06 · Test 1: Lichtsensor einzeln prüfen

LERNZIEL:
- Passende Schwellenwerte für eure Umgebung finden.

HARDWARE: siehe ANLEITUNG.md (Fotowiderstand an GPIO 28)

VORGEHEN:
1. Skript starten (F5).
2. Hand über den Sensor halten -> kleine Werte ablesen.
3. Zimmerlicht           -> mittlere Werte.
4. Handytaschenlampe     -> große Werte.
5. Werte notieren und in 03_alarmanlage_gesamt.py eintragen.
"""

from machine import ADC, Pin
from utime import sleep

adc = ADC(Pin(28))

print("Lichtsensor-Test gestartet…")
print("Strg + C zum Beenden.")

while True:
    wert = adc.read_u16()
    print("Lichtwert:", wert)
    sleep(1)
