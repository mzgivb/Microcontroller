"""
Lektion 1.1: Interne LED blinken lassen

LERNZIELE:
- Einen GPIO-Pin als Ausgang setzen
- Eine Endlosschleife verwenden (while True)
- Warten mit sleep()

PYTHON-KONZEPTE:
- import: andere Module laden
- Pin(nummer, richtung): GPIO konfigurieren
- while True: wiederhole für immer

HARDWARE:
- Nur der Raspberry Pi Pico H, kein Breadboard nötig.
- Die interne LED hängt an GPIO 25.
"""

from machine import Pin
from utime import sleep

# GPIO 25 = interne LED auf dem Pico H
led = Pin(25, Pin.OUT)

while True:
    led.value(1)   # LED an  (HIGH = 3,3 V)
    sleep(0.5)     # warte 0,5 Sekunden
    led.value(0)   # LED aus (LOW  = 0 V)
    sleep(0.5)


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Lass die LED schneller blinken (kleinere Zahl bei sleep).
#
# 2. Lass die LED langsamer blinken (größere Zahl bei sleep).
#
# 3. VORHERSAGE: Was passiert, wenn du sleep(0) schreibst?
#    Testet es – könnt ihr das Licht noch flackern sehen?
#
# 4. Ersetze `led.value(1)` durch `led.on()` und `led.value(0)`
#    durch `led.off()`. Funktioniert das Programm genauso?
# ============================================================
