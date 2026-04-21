"""
Lektion 2.3: Potentiometer auslesen (ADC)

LERNZIELE:
- Was ein ADC (Analog-Digital-Wandler) macht
- Messwerte skalieren und anzeigen

PYTHON-KONZEPTE:
- ADC.read_u16() liefert Zahlen von 0 bis 65535
- Berechnungen mit float

HARDWARE:
- Potentiometer 10 kΩ (3 Beine)
- Außen: 3V3 und GND
- Mitte (Schleifer): GPIO 26 (ADC0, Pin 31)

VERKABELUNG:
  Poti Pin 1 (links)   ──── 3V3  (Pin 36)
  Poti Pin 2 (Mitte)   ──── GPIO 26 / ADC0 (Pin 31)
  Poti Pin 3 (rechts)  ──── GND  (Pin 38)
"""

from machine import ADC, Pin
from utime import sleep

poti = ADC(Pin(26))

while True:
    rohwert = poti.read_u16()                 # 0 … 65535
    prozent = (rohwert / 65535) * 100         # 0,0 … 100,0
    print("Rohwert:", rohwert, "  Prozent:", round(prozent, 1), "%")
    sleep(0.2)


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Rechne den Wert in eine Spannung in Volt um (0 … 3,3 V).
#
# 2. Schließe eine LED an GPIO 15 an. Steuere ihre Helligkeit
#    mit dem Poti -- Tipp: PWM (siehe Lektion 03).
#
# 3. Nutze das Poti als "Lautstärke-Regler" für den Buzzer
#    aus Lektion 03.
#
# 4. CHALLENGE: Schreibe die letzten 10 Messwerte in eine Liste
#    und berechne den Mittelwert (Glättung).
# ============================================================
