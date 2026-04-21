# Lektion 03 · Ausgaben – Buzzer und OLED-Display

Bis hierhin haben wir nur LEDs geschaltet. Jetzt wird die Palette größer:
ein **Piezo-Buzzer** macht Töne, ein **OLED-Display** zeigt Texte.

## Lernziele

- **PWM** (Pulsweitenmodulation) verstehen und anwenden
- Den **I²C-Bus** einsetzen, um einen Chip anzusprechen
- Eigene **Funktionen** schreiben

## Bibliotheken

Vor dieser Lektion muss `lib/ssd1306.py` auf den Pico kopiert sein.
Siehe [../../SETUP.md](../../SETUP.md) Abschnitt 3.

## Dateien

| Datei | Thema |
|-------|-------|
| `01_buzzer_ton.py` | Ton über PWM erzeugen |
| `02_oled_hallo_welt.py` | Text auf dem OLED anzeigen |
| `03_melodie_spielen.py` | Funktion und Tonhöhen kombinieren |
