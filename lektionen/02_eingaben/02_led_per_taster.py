"""
Lektion 2.2: LED per Taster steuern

LERNZIELE:
- Zwei GPIOs gleichzeitig nutzen (ein Ein-, ein Ausgang)
- Ein Mini-Programm aus Bedingungen bauen

PYTHON-KONZEPTE:
- Wiederholung aus 2.1 + 1.3
- Zwei Variablen in einer while-Schleife

HARDWARE:
- Taster an GPIO 14 (zu GND)
- LED an GPIO 15 (mit 220 Ω Vorwiderstand, zu GND)

VERKABELUNG:
  siehe verkabelung_02_02.md
"""

from machine import Pin

taster = Pin(14, Pin.IN, Pin.PULL_UP)
led = Pin(15, Pin.OUT)

while True:
    if taster.value() == 0:   # Taster gedrückt
        led.value(1)
    else:
        led.value(0)


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Kehre das Verhalten um: LED leuchtet, wenn Taster NICHT
#    gedrückt ist.
#
# 2. Zwei Taster steuern zwei LEDs unabhängig.
#
# 3. Taster-TOGGLE: Mit jedem Druck soll die LED umschalten
#    (an -> aus -> an -> aus ...). Tipp: merk dir den letzten
#    Zustand in einer Variablen.
#
# 4. CHALLENGE: Mit einem Taster drei LEDs steuern:
#    1x drücken = rot, 2x = gelb, 3x = grün.
# ============================================================
