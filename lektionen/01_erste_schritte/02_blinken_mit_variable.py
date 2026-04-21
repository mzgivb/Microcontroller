"""
Lektion 1.2: Blinken mit einer Variablen

LERNZIELE:
- Variablen einsetzen, um Werte zentral zu ändern
- Wiederholungen mit einer Zählschleife (for)

PYTHON-KONZEPTE:
- Variable = Wert
- for i in range(n): wiederhole n-mal
- input(): Wert vom Benutzer einlesen

HARDWARE:
- Wie in 1.1: interne LED, kein Breadboard.
"""

from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)

# Wert aus dem Thonny-Terminal lesen und in eine Zahl umwandeln
anzahl = int(input("Wie oft soll die LED blinken? "))

# Variable für die Blinkgeschwindigkeit (in Sekunden)
pause = 0.3

# for-Schleife: wiederhole "anzahl"-mal
for i in range(anzahl):
    print("Blink Nr.", i + 1)
    led.value(1)
    sleep(pause)
    led.value(0)
    sleep(pause)

print("Fertig!")


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Ändere den Wert von "pause", ohne den Rest anzufassen.
#    Wie wirkt sich das aus?
#
# 2. Lasse die LED abwechselnd lang und kurz blinken
#    (Tipp: zwei verschiedene sleep-Zeiten).
#
# 3. Fordere zusätzlich die Pause-Zeit per input() ab
#    (achte auf float() statt int()).
#
# 4. Schreibe ein SOS-Signal im Morse-Code (... --- ...).
# ============================================================
