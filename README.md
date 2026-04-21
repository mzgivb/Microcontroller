# Mikrocontroller – Projektwoche mit dem Raspberry Pi Pico H

Willkommen! Dieses Repository enthält einen kompletten Workshop zum Programmieren
von Mikrocontrollern mit **MicroPython** und dem **Raspberry Pi Pico H**.

**Zielgruppe:** Klasse 7–10
**Fächer:** Informatik (fächerübergreifend mit Physik / NaWi)
**Dauer:** 5-Tage-Projektwoche (an kürzere/längere Formate anpassbar)

---

## Lernpfad

| Lektion | Thema | Python-Konzepte | Hardware |
|---------|-------|-----------------|----------|
| **01** | [Erste Schritte – LED](lektionen/01_erste_schritte/) | Variablen, `while`, `sleep` | Interne + externe LED |
| **02** | [Eingaben](lektionen/02_eingaben/) | `if/else`, Pull-Up, ADC | Taster, Potentiometer |
| **03** | [Ausgaben](lektionen/03_ausgaben/) | Funktionen, PWM, I2C | Buzzer, OLED-Display |
| **04** | [Sensoren](lektionen/04_sensoren/) | Schwellenwerte, Listen | Lichtsensor, DHT11 |
| **05** | 🌧️ [Projekt Wetterstation](lektionen/05_projekt_wetterstation/) | Alles Bisherige | DHT11 + OLED |
| **06** | 🍬 [Projekt Süßigkeitenalarm](lektionen/06_projekt_alarmanlage/) | Alles Bisherige | Fotowiderstand + Buzzer |
| **07** | 💡 [Eigenes Projekt](lektionen/07_eigenes_projekt/) | freie Wahl | frei |

## Schnellstart

1. **Pico vorbereiten** → siehe [SETUP.md](SETUP.md) (MicroPython flashen, Thonny einrichten)
2. **Bibliotheken** aus [`lib/`](lib/) auf den Pico kopieren (nur nötig für Lektion 03+)
3. **Lektion 01 öffnen**, Datei in Thonny starten (F5) und loslegen

```python
from machine import Pin
from utime import sleep

led = Pin(25, Pin.OUT)   # interne LED des Pico

while True:
    led.value(1)
    sleep(0.5)
    led.value(0)
    sleep(0.5)
```

## Hardware

Pro Schüler:in bzw. pro Gruppe wird ein **Klassenset Pico H** benötigt.
Komplette Stückliste mit Bezugsquellen → [HARDWARE.md](HARDWARE.md).

Kurzform pro Arbeitsplatz:
- 1× Raspberry Pi Pico H (mit Stiftleisten)
- 1× Breadboard, Jumperkabel
- LEDs, Widerstände (220 Ω, 10 kΩ), Taster
- 1× OLED SSD1306 (128×64, I²C), 1× Piezo-Buzzer
- 1× DHT11, 1× Fotowiderstand, 1× Potentiometer

## Für Lehrkräfte

Eine Woche vor der Projektwoche sollten alle Lehrkräfte die Lektionen **einmal
selbst durchlaufen**. Der vollständige Vorbereitungs- und Tagesablauf-Leitfaden
steht in **[FÜR_LEHRKRÄFTE.md](FÜR_LEHRKRÄFTE.md)**.

## Didaktisches Prinzip

Jede `.py`-Datei in diesem Repo hat denselben Aufbau:

- **Lernziele** am Anfang (Was können die SuS danach?)
- **Python-Konzepte** (Was ist neu gegenüber der vorigen Lektion?)
- **Hardware / Verkabelung** (Was muss gesteckt werden?)
- **Kommentierter Code** auf Deutsch
- **Aufgaben zum Ausprobieren** am Ende (Differenzierung!)

Empfohlene Vorgehensweise im Unterricht:
1. Code gemeinsam lesen, Vorhersagen treffen („Was wird passieren?")
2. Ausführen und beobachten
3. Variationen ausprobieren (Aufgaben-Block)
4. Eigene Idee entwickeln

## Sicherheit

- Immer den Pico vom USB trennen, bevor etwas am Breadboard umgesteckt wird
- 3V3 und GND **nicht** vertauschen
- LEDs **immer** mit Vorwiderstand (220 Ω) betreiben
- Kein Löten im Regelbetrieb – nur Breadboard-Aufbauten

## Historische Arduino-Nano-ESP32-Version

Die ursprüngliche ESP32-Variante der Skripte liegt im Ordner
[`legacy_esp32/`](legacy_esp32/). Für die Projektwoche wird auf Pico H migriert,
weil dort bereits erprobte Workshop-Materialien (Wetterstation, Alarmanlage)
existieren.

## Lizenz

Das Material ist frei für Bildungszwecke verwendbar.
