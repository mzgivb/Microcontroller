"""
Lektion 1.3: Externe LED am Breadboard

LERNZIELE:
- Eine LED korrekt mit Vorwiderstand anschließen
- Unterschied zwischen interner und externer LED verstehen

PYTHON-KONZEPTE:
- Wiederholung aus 1.1, nur auf anderen Pin

HARDWARE:
- Raspberry Pi Pico H
- Breadboard
- 1× LED (beliebige Farbe)
- 1× 220 Ω Widerstand (orange-orange-braun)
- 2× Jumperkabel

VERKABELUNG:
  Pico GPIO 15 (Pin 20)  ──── 220 Ω Widerstand ──── LED Anode (langes Bein)
  LED Kathode (kurzes Bein, abgeflachte Seite)  ──── Pico GND (Pin 23 oder 38)

  ACHTUNG:
  - LED hat eine Richtung! Kurzes Bein = Minus.
  - OHNE Vorwiderstand brennt die LED durch!

  Schaltplan:  assets/verkabelung_01_03.md (siehe Lektionsordner)
"""

from machine import Pin
from utime import sleep

# Externe LED an GPIO 15 (Pin 20 am Pico)
led = Pin(15, Pin.OUT)

while True:
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(1)


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Schließe eine ZWEITE LED an GPIO 14 an.
#    Lass beide abwechselnd blinken (wie ein Martinshorn).
#
# 2. Schließe drei LEDs an (rot, gelb, grün) und programmiere
#    eine Ampel: rot -> rot+gelb -> grün -> gelb -> rot ...
#
# 3. Kombiniere interne und externe LED:
#    Die interne LED blinkt doppelt so schnell wie die externe.
#
# 4. CHALLENGE: Programmiere eine Lauflicht-Kette aus 4 LEDs
#    (wie beim Kitt-Auto aus Knight Rider).
# ============================================================
