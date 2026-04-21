# Projekt 06 · 🍬 Süßigkeiten-Alarmanlage

Ihr baut eine Box, die Alarm schlägt, sobald jemand den Deckel öffnet und
**Licht** auf den Sensor im Inneren fällt. Perfekt, um die Naschereien vor
(kleinen und großen) Diebinnen und Dieben zu schützen.

> Dieses Projekt baut auf Lektion 02 (ADC), 03 (Buzzer) und 04 (Lichtsensor) auf.

## Wie funktioniert's?

| Zustand | Licht am Sensor | Programm |
|---------|-----------------|----------|
| Box geschlossen | dunkel | Alles ruhig |
| Box geöffnet | hell | Alarm piept 10 Sekunden |
| Wieder zu | dunkel | Alarm schweigt |

## Bauteile

- 1× Raspberry Pi Pico H
- 1× Fotowiderstand (LDR)
- 1× 10 kΩ Widerstand
- 1× Piezo-Buzzer
- Breadboard + Jumperkabel
- 1× Box (Schuhkarton, Holzkiste, 3D-Druck)
- Klebeband / Heißkleber

## Dateien

| Datei | Reihenfolge |
|-------|-------------|
| `ANLEITUNG.md` | Schritt-für-Schritt-Bauanleitung |
| `01_lichtsensor_testen.py` | Erst einzeln den Sensor prüfen |
| `02_buzzer_testen.py` | Dann den Buzzer |
| `03_alarmanlage_gesamt.py` | Beides zusammen – das fertige Projekt |

**Warum drei Dateien?** Wenn am Ende etwas nicht geht, findet ihr viel
einfacher den Fehler, wenn ihr vorher jedes Bauteil **einzeln** getestet habt.
