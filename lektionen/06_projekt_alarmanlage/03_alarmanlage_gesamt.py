"""
Projekt 06: Süßigkeiten-Alarmanlage (komplett)

LERNZIELE:
- Zwei Eingaben/Ausgaben sinnvoll verbinden
- Schwellenwerte nutzen, um Zustände zu erkennen
- Eine Zustandslogik schreiben (offen/geschlossen)

HARDWARE:
- LDR an GPIO 28 (siehe Anleitung)
- Buzzer an GPIO 15

HINWEIS:
  Tragt eure eigenen Schwellenwerte aus 01_lichtsensor_testen.py ein!
"""

from machine import ADC, Pin, PWM
from utime import sleep

# --- Hardware ---------------------------------------------------
adc    = ADC(Pin(28))
buzzer = PWM(Pin(15))
buzzer.freq(1000)
buzzer.duty_u16(0)

# --- Schwellenwerte (bitte anpassen!) ---------------------------
SCHWELLE_OFFEN       = 10000   # darunter = dunkel   = Box zu
SCHWELLE_GESCHLOSSEN = 25000   # darüber  = hell     = Box auf


def ton_an():
    buzzer.duty_u16(32768)

def ton_aus():
    buzzer.duty_u16(0)


print("Alarmanlage aktiv. Box zu = Ruhe, Box offen = ALARM.")

while True:
    wert = adc.read_u16()
    print("Lichtwert:", wert)

    if wert > SCHWELLE_GESCHLOSSEN:
        # Box ist offen -> Alarm für 10 Sekunden
        print("ALARM! Box ist offen!")
        ton_an()
        sleep(10)
        ton_aus()
        print("Alarm beendet.")
    elif wert < SCHWELLE_OFFEN:
        # Box ist definitiv zu
        ton_aus()

    sleep(0.1)
