"""
Lektion 4.1: Fotowiderstand (LDR)

LERNZIELE:
- Einen analogen Sensor mit Spannungsteiler auslesen
- Rohwerte interpretieren (hell / dunkel)

PYTHON-KONZEPTE:
- ADC (wie Lektion 2.3)
- if / elif / else mit Schwellenwerten

HARDWARE:
- Fotowiderstand (LDR, z.B. GL5528)
- 10 kΩ Widerstand (als Spannungsteiler-Partner)

VERKABELUNG (Spannungsteiler):
  3V3 ──── LDR ──┬── GPIO 28 (ADC2, Pin 34)
                 │
               10 kΩ
                 │
                GND

  Hell: LDR hat niedrigen Widerstand  -> Spannung am Pin hoch   -> Wert groß
  Dunkel: LDR hat hohen Widerstand    -> Spannung am Pin niedrig -> Wert klein
  (Die Richtung kann sich bei anderer Verdrahtung umkehren!)
"""

from machine import ADC, Pin
from utime import sleep

ldr = ADC(Pin(28))

while True:
    wert = ldr.read_u16()    # 0 … 65535

    if wert < 10000:
        zustand = "dunkel"
    elif wert < 30000:
        zustand = "normal"
    else:
        zustand = "HELL!"

    print("Wert:", wert, "->", zustand)
    sleep(0.5)


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Findet eure eigenen Schwellenwerte: messt mit abgedecktem
#    Sensor, mit Zimmerlicht und mit Handytaschenlampe.
#
# 2. Lasst eine LED aufleuchten, sobald es dunkel wird
#    (z.B. beim Abdecken des Sensors).
#
# 3. Lasst den Buzzer piepen, sobald es sehr hell wird.
#    -> Damit habt ihr schon 80% der Alarmanlage aus Projekt 06!
#
# 4. CHALLENGE: Zeigt den aktuellen Helligkeitswert als Balken
#    auf dem OLED an (display.fill_rect verwenden).
# ============================================================
