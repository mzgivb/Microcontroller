# Projekt 05 · 🌧️ Wetterstation

Ihr baut eine kleine Wetterstation, die **Temperatur** und
**Luftfeuchtigkeit** misst und direkt auf einem OLED-Display anzeigt –
ganz ohne Computer, sobald sie läuft.

> Dieses Projekt baut auf den Lektionen 03 (OLED) und 04 (DHT11) auf.

## Was lernst du?

- Wie man mehrere Sensoren und Ausgaben kombiniert
- Wie man Messwerte aufbereitet darstellt
- Wie man den Code so strukturiert, dass er dauerhaft läuft

## Bauteile

- 1× Raspberry Pi Pico H
- 1× DHT11 Temperatur-/Feuchte-Sensor (3-Pin-Modul)
- 1× OLED-Display SSD1306 128×64 (I²C)
- 1× Breadboard + Jumperkabel

## Verkabelung

| Bauteil | Pico-Pin |
|---------|----------|
| DHT11 Signal (S) | GPIO 13 (Pin 17) |
| DHT11 VCC | 3V3 (Pin 36) |
| DHT11 GND | GND (Pin 38) |
| OLED SDA | GPIO 16 (Pin 21) |
| OLED SCL | GPIO 17 (Pin 22) |
| OLED VCC | 3V3 (Pin 36) |
| OLED GND | GND (Pin 38) |

Mehrere 3V3- und GND-Pins könnt ihr über die **Stromschienen am Breadboard**
verteilen. Siehe `ANLEITUNG.md` für die Schritt-für-Schritt-Anleitung.

## Dateien

| Datei | Zweck |
|-------|-------|
| `ANLEITUNG.md` | Ausführliche Schritt-für-Schritt-Anleitung |
| `wetterstation.py` | Fertiges Programm |
| `erweiterungen.md` | Ideen für eigene Weiterentwicklungen |
