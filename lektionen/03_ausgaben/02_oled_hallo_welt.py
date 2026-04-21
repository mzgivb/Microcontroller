"""
Lektion 3.2: OLED-Display – "Hallo Welt"

LERNZIELE:
- I²C einrichten und verstehen
- Text auf einem grafischen Display ausgeben
- Die SSD1306-Bibliothek benutzen

PYTHON-KONZEPTE:
- Klassen nutzen (display.text, display.show)
- I²C-Scan zur Fehlersuche

VORAUSSETZUNG:
  lib/ssd1306.py muss auf dem Pico liegen! (siehe SETUP.md)

HARDWARE:
- OLED SSD1306 128x64 mit I²C-Anschluss (4 Pins)

VERKABELUNG:
  OLED VCC  ──── Pico 3V3  (Pin 36)
  OLED GND  ──── Pico GND  (Pin 38)
  OLED SDA  ──── Pico GPIO 16 (Pin 21)
  OLED SCL  ──── Pico GPIO 17 (Pin 22)
"""

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# I²C-Bus 0 an den genannten Pins aufbauen
i2c = I2C(0, scl=Pin(17), sda=Pin(16), freq=400000)

# Kontrolle: welche Adressen antworten auf dem Bus?
print("I2C-Scan:", [hex(a) for a in i2c.scan()])

# Typische Adresse = 0x3C. Falls dein Display 0x3D meldet:
# display = SSD1306_I2C(128, 64, i2c, addr=0x3D)
display = SSD1306_I2C(128, 64, i2c)

display.fill(0)                     # Bildschirm löschen
display.text("Hallo Welt!", 0, 0)   # x=0, y=0 (links oben)
display.text("Pico H rockt", 0, 20)
display.show()                      # sichtbar machen!


# ============================================================
# AUFGABEN ZUM AUSPROBIEREN
# ============================================================
# 1. Verändere die Koordinaten so, dass der Text mittig steht.
#    Tipp: eine Zeile ist 8 Pixel hoch, ein Zeichen 8 Pixel breit.
#
# 2. Zeige deinen Namen in der Mitte, darüber einen Rahmen mit
#    display.rect(x, y, breite, hoehe, 1).
#
# 3. Zeichne einen Kreis in die Ecke. Tipp:
#    for w in range(0, 360): setze pixel mit sin/cos ...
#    (ohne Kreis-Funktion -- das ist die Aufgabe!)
#
# 4. CHALLENGE: Tastendruck-Zähler aus Lektion 02 auf dem OLED
#    statt im Terminal anzeigen.
# ============================================================
