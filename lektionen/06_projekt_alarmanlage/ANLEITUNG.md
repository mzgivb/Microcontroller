# Süßigkeiten-Alarmanlage – komplette Bauanleitung

> Basiert auf dem erprobten Workshop-Material "🍭 Suessigkeitenalarmanlage".

## Schaltung auf dem Breadboard

### Schritt 1 – Pico aufstecken

Pico H mittig auf das Breadboard stecken, USB-Port zeigt nach außen.

### Schritt 2 – Fotowiderstand-Schaltung

Ein Bein des Fotowiderstands über ein **rotes Kabel** an **3V3** (Pin 36).
Das andere Bein an **GPIO 28** (Pin 34). Vom selben Punkt geht zusätzlich
ein **10 kΩ Widerstand** zu **GND** (Pin 38).

```
3V3 ─── LDR ──┬── GPIO 28 (ADC2)
              │
           10 kΩ
              │
             GND
```

### Schritt 3 – Buzzer

- Plus (rot) → GPIO 15 (Pin 20)
- Minus (schwarz) → GND (Pin 23 oder 38)

### Schritt 4 – Verkabelung prüfen

- Alle **roten** Kabel gehen zu 3V3
- Alle **schwarzen** Kabel gehen zu GND
- Signalleitungen (grün) gehen zu GPIO 28 und GPIO 15

## Programm testen

### Test 1 – nur der Lichtsensor

`01_lichtsensor_testen.py` in Thonny ausführen. Beobachtet die ausgegebenen
Werte im Terminal:

- **Hand über den Sensor** → kleine Werte (dunkel)
- **Normales Zimmerlicht** → mittlere Werte (10 000 – 30 000)
- **Handy-Taschenlampe** → große Werte (> 40 000)

Notiert euch eure eigenen Schwellenwerte!

### Test 2 – nur der Buzzer

`02_buzzer_testen.py` ausführen. Ihr solltet 2 Sekunden lang einen Piepton
hören.

### Test 3 – Alarmanlage komplett

Wenn beide Einzeltests klappen, `03_alarmanlage_gesamt.py` ausführen.

- Box geschlossen (Sensor abgedeckt) → Ruhe
- Box geöffnet → Alarm!

## In die Box einbauen

- **Fotowiderstand** oben am Deckel befestigen, so dass er bei geschlossener
  Box dunkel ist und bei geöffnetem Deckel Licht abbekommt.
- **Buzzer** seitlich ankleben (nicht direkt unter den Fotowiderstand).
- **Pico und Breadboard** am Boden mit doppelseitigem Klebeband fixieren.
- **USB-Kabel** durch ein Loch im Karton nach außen führen.

## Tipps

- **Alarmton verändern:** `buzzer.freq(500)` oder `buzzer.freq(2000)` ausprobieren.
- **Alarmdauer ändern:** `sleep(10)` auf `sleep(5)` oder `sleep(30)` setzen.
- **Schwellenwerte anpassen:** Im Code die Konstanten `SCHWELLE_OFFEN` und
  `SCHWELLE_GESCHLOSSEN` auf die Werte aus Test 1 setzen.

## Troubleshooting

| Problem | Lösung |
|---------|--------|
| Kein Ton | Buzzer-Verkabelung prüfen (rot an GPIO 15, schwarz an GND) |
| Alarm kommt nie | Mit Handytaschenlampe testen, Schwellenwert evtl. zu hoch |
| Alarm hört nicht auf | Schwellenwerte umgekehrt? `SCHWELLE_GESCHLOSSEN` muss größer sein als `SCHWELLE_OFFEN` |
| Sensor-Werte zittern stark | `time.sleep(0.1)` zwischen Messungen |
| Programm hängt | USB-Kabel ab- und wieder anstecken, in Thonny neu starten |

## Erweiterungen

- **LED dazu:** Blinkt synchron zum Alarm.
- **Mehrere Töne:** Statt eines Piepens eine kurze Melodie wie ein Martinshorn
  (siehe `lektionen/03_ausgaben/03_melodie_spielen.py`).
- **Passwort zum Deaktivieren:** Tasterfolge (z.B. 3× kurz, 1× lang).
- **Display "FINGER WEG!":** OLED aus Lektion 03 einbinden.
- **Abstufungen:** Je heller, desto schneller piept der Alarm (Poti-Theremin-
  Effekt).
