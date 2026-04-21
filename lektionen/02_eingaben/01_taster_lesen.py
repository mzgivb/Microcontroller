"""
Lektion 2.1: Taster lesen

LERNZIELE:
- Einen GPIO-Pin als Eingang konfigurieren
- Wie ein Pull-Up-Widerstand funktioniert
- Tastendrücke im Terminal sichtbar machen

PYTHON-KONZEPTE:
- Pin.IN mit Pin.PULL_UP
- if / else
- print() zur Ausgabe

HARDWARE:
- Taster: ein Bein an GPIO 14 (Pin 19), anderes Bein an GND.
- Mehr ist nicht nötig! Der Pico hat eingebaute Pull-Up-Widerstände.

VERKABELUNG:
  Pico GPIO 14 (Pin 19) ──── Taster ──── GND (Pin 18)

PULL-UP ERKLÄRT:
  Ein Eingang ohne Pull-Up wäre "frei" und würde zufällige Werte liefern.
  Der interne Pull-Up zieht den Pin auf 3,3 V (HIGH = 1), solange der Taster
  offen ist. Beim Druck verbindet der Taster den Pin mit GND -> LOW (0).
"""

from machine import Pin
from utime import sleep

taster = Pin(14, Pin.IN, Pin.PULL_UP)

while True:
    if taster.value() == 0:
        print("Taster GEDRÜCKT")
    else:
        print("Taster offen")
    sleep(0.2)


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Schließe einen zweiten Taster an GPIO 13 an. Gib für beide
#    Taster getrennte Meldungen aus.
#
# 2. Zähle, wie oft der Taster gedrückt wurde. Zeige die Zahl
#    nach jedem Druck im Terminal an.
#
# 3. VORHERSAGE: Was passiert, wenn ihr den Pull-Up weglasst,
#    also Pin(14, Pin.IN) schreibt? (Testet es – vorsichtig!)
# ============================================================
