# Setup – Pico H startklar machen

In diesem Dokument wird Schritt für Schritt erklärt, wie der Raspberry Pi Pico H
für die Projektwoche vorbereitet wird. Zeitbedarf: ca. **20 Minuten**.

---

## 1 · Thonny installieren

**Thonny** ist eine einfache Python-Entwicklungsumgebung, die MicroPython direkt
auf dem Pico ausführen kann.

1. Öffne **[thonny.org](https://thonny.org)**.
2. Lade die passende Version für dein Betriebssystem (Windows / macOS / Linux).
3. Installiere Thonny und starte es.

---

## 2 · MicroPython auf den Pico flashen

Ein neuer Pico H hat noch kein MicroPython. Das muss einmalig installiert
werden – danach bleibt es drauf.

1. **BOOTSEL-Taste** am Pico gedrückt halten und dabei das USB-Kabel in den
   Computer stecken.
2. Der Pico erscheint als USB-Laufwerk namens **`RPI-RP2`**.
3. In Thonny: Menü **Ausführen → Interpreter wechseln → MicroPython (Raspberry Pi Pico)**.
4. Thonny öffnet einen Dialog und fragt: *„MicroPython installieren?"* → **Ja**.
5. Warten, bis die Meldung "Installation abgeschlossen" erscheint (ca. 1 Minute).

Alternative: `.uf2`-Datei manuell von
[micropython.org/download/RPI_PICO/](https://micropython.org/download/RPI_PICO/)
herunterladen und per Drag-and-Drop auf das `RPI-RP2`-Laufwerk ziehen.

---

## 3 · Bibliotheken auf den Pico kopieren

Für die Lektionen 03–06 werden zusätzliche Python-Bibliotheken auf dem Pico
gebraucht. Sie liegen im Ordner [`lib/`](lib/) dieses Repos.

1. In Thonny den Ordner [`lib/`](lib/) öffnen (z.B. per "Datei → Öffnen…").
2. Rechtsklick auf `ssd1306.py` → **„Auf /“-Speicher hochladen“**.
3. Das Gleiche für `lcd_api.py` und `i2c_lcd.py` (nur falls LCD benutzt wird).

Kontrolle: In Thonny unten links → "Dateien" → "Raspberry Pi Pico" – dort
müssen die Dateien jetzt liegen.

---

## 4 · Erste Verbindung testen

1. Neue Datei in Thonny öffnen.
2. Folgendes tippen:

```python
print("Hallo Pico!")
```

3. **F5** drücken (oder Play-Button).
4. Im unteren Terminal erscheint: `Hallo Pico!`

✅ Wenn das funktioniert, ist alles bereit für **Lektion 01**.

---

## 5 · Troubleshooting

| Problem | Lösung |
|---------|--------|
| `RPI-RP2` erscheint nicht | Anderes USB-Kabel (Datenkabel!) oder anderer USB-Port |
| Thonny findet den Pico nicht | Menü „Ausführen → Interpreter wechseln → MicroPython (Raspberry Pi Pico)" |
| Nach dem Flashen friert Thonny ein | Einmal USB ab- und wieder anstecken |
| Datei soll automatisch beim Einstecken starten | Datei als **`main.py`** auf dem Pico speichern |
| „Permission denied" (Linux) | User zur Gruppe `dialout` hinzufügen: `sudo usermod -aG dialout $USER`, dann neu anmelden |

---

## 6 · Pico mit voreingerichtetem Master-Image duplizieren (Lehrkräfte)

Wenn viele Picos vorzubereiten sind, lohnt sich folgender Trick:

1. Einen Pico als **Master** einrichten (MicroPython + Bibliotheken aus [`lib/`](lib/)).
2. In Thonny: Dateien anzeigen, alle benötigten Dateien identifizieren.
3. Für jeden weiteren Pico:
   - Neu flashen (Schritt 2)
   - In Thonny die Bibliotheks-Dateien per Rechtsklick hochladen

Das dauert pro Gerät ca. 2 Minuten – bei 15 Picos also eine halbe Stunde.
