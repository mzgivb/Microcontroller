"""
Lektion 3.3: Eine Melodie spielen

LERNZIELE:
- Eigene Funktionen schreiben
- Listen verwenden
- Tonhöhen über Notennamen nutzen

PYTHON-KONZEPTE:
- def funktionsname(parameter): ...
- dict = {Name: Wert}
- for note in melodie: ...

HARDWARE:
- Wie in 3.1 (Buzzer an GPIO 15)
"""

from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))

# Frequenz-Tabelle einiger Noten (in Hz)
NOTEN = {
    "C":  262,
    "D":  294,
    "E":  330,
    "F":  349,
    "G":  392,
    "A":  440,
    "H":  494,
    "C2": 523,
    "-":  0,     # Pause
}


def spiele_note(name, dauer):
    """Spielt genau eine Note (name = Eintrag aus NOTEN)."""
    freq = NOTEN[name]
    if freq > 0:
        buzzer.freq(freq)
        buzzer.duty_u16(32768)
    else:
        buzzer.duty_u16(0)
    sleep(dauer)
    buzzer.duty_u16(0)
    sleep(0.05)   # kurze Trennpause zwischen Noten


# Melodie: "Alle meine Entchen"
MELODIE = [
    ("C", 0.4), ("D", 0.4), ("E", 0.4), ("F", 0.4),
    ("G", 0.8), ("G", 0.8),
    ("A", 0.4), ("A", 0.4), ("A", 0.4), ("A", 0.4),
    ("G", 1.6),
]

for note, dauer in MELODIE:
    spiele_note(note, dauer)

print("Fertig!")


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Spielt die Melodie doppelt so schnell (Dauer halbieren).
#
# 2. Fügt "Alle meine Entchen" den Text der zweiten Zeile hinzu
#    ("schwimmen auf dem See ...") -- schaut die Noten nach.
#
# 3. Schreibt eine eigene Melodie (4-8 Takte).
#
# 4. CHALLENGE: Lasst den Melodie-Start per Taster auslösen
#    (Lektion 02 kombinieren).
# ============================================================
