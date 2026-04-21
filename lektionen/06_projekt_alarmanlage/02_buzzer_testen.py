"""
Projekt 06 · Test 2: Buzzer einzeln prüfen

LERNZIEL:
- Sicherstellen, dass der Buzzer klingt, bevor wir ihn in die
  Alarmanlage einbauen.

HARDWARE:
- Buzzer + an GPIO 15, Buzzer - an GND.
"""

from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))
buzzer.freq(1000)        # 1000 Hz -- typischer Alarmton
buzzer.duty_u16(32768)   # ~halbe Lautstärke
sleep(2)
buzzer.duty_u16(0)       # aus

print("Buzzer-Test abgeschlossen.")
