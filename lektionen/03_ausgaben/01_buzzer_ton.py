"""
Lektion 3.1: Buzzer – Töne mit PWM

LERNZIELE:
- PWM (Pulsweitenmodulation) kennenlernen
- Frequenz und Lautstärke unterscheiden

PYTHON-KONZEPTE:
- PWM(Pin) erzeugt ein schnelles Ein/Aus-Signal
- buzzer.freq(hz)  = Tonhöhe (Hz)
- buzzer.duty_u16(v) = Lautstärke (0 = aus, 32768 = ~50 %, 65535 = max)

HARDWARE:
- Passiver Piezo-Buzzer
- +  (rot)   → GPIO 15 (Pin 20)
- -- (schw.) → GND    (Pin 23)

HINWEIS:
  Aktive Buzzer haben einen festen Ton. Für diese Lektion brauchst du einen
  passiven Buzzer, bei dem du die Tonhöhe selbst einstellen kannst.
"""

from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))
buzzer.duty_u16(0)            # erstmal stumm schalten

# Ein kurzer Piep bei 1000 Hz (A-Kammerton wäre 440 Hz)
buzzer.freq(1000)
buzzer.duty_u16(32768)        # ~ halbe Lautstärke
sleep(0.5)
buzzer.duty_u16(0)            # aus

sleep(0.5)

# Jetzt ein höherer Ton
buzzer.freq(2000)
buzzer.duty_u16(32768)
sleep(0.5)
buzzer.duty_u16(0)


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Probiere verschiedene Frequenzen aus:
#    220, 440, 880, 1760 Hz -- was stellst du fest?
#
# 2. Ändere die Lautstärke mit duty_u16(): 8192, 32768, 49152.
#
# 3. Schreibe eine Sirene: Ton steigt von 500 Hz auf 2000 Hz
#    und fällt zurück (for-Schleife mit range).
#
# 4. CHALLENGE: Kombiniere Poti (Lektion 2.3) + Buzzer zu einem
#    "Theremin": Poti-Stellung bestimmt die Tonhöhe live.
# ============================================================
