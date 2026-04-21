# Wetterstation – Schritt für Schritt

> Basiert auf dem lokalen Workshop-Material "Wetterstation mit Pico H bauen".

## Was baust du?

Eine kleine Wetterstation mit DHT11-Sensor und OLED-Display. Sobald sie mit
Strom versorgt wird, zeigt sie Temperatur und Luftfeuchtigkeit im Raum an.

## Sensoren und Display verstehen

### DHT11

- Temperatur: 0–50 °C (±2 °C)
- Luftfeuchte: 20–80 % (±5 %)
- Digitaler Sensor mit Pull-Up auf dem Modul → kein externer Widerstand nötig
- Messungen max. alle **2 Sekunden** möglich

### OLED SSD1306

- 128×64 Pixel, I²C-Adresse meist `0x3C`
- 4 Pins: VCC, GND, SDA, SCL
- Sehr kontraststark, benötigt kein Hintergrundlicht

## Verkabelung Schritt für Schritt

1. **Pico vom USB trennen.**
2. Pico mittig auf das Breadboard stecken (USB-Port zeigt nach außen).
3. 3V3 vom Pico (Pin 36) auf die rote Stromschiene des Breadboards führen.
4. GND vom Pico (Pin 38) auf die blaue Stromschiene führen.
5. **DHT11 verbinden:**
   - GND (Pin „−") → blaue Schiene
   - VCC (Pin „+") → rote Schiene
   - Data (Pin „S") → GPIO 13 (Pin 17)
6. **OLED verbinden:**
   - VCC → rote Schiene
   - GND → blaue Schiene
   - SDA → GPIO 16 (Pin 21)
   - SCL → GPIO 17 (Pin 22)
7. Sichtkontrolle! Dann Pico wieder per USB anschließen.

## Programm

1. `wetterstation.py` in Thonny öffnen
2. Mit **F5** starten
3. Auf dem OLED solltest du Temperatur und Feuchte sehen

## Troubleshooting

| Problem | Ursache | Lösung |
|---------|---------|--------|
| OLED bleibt schwarz | Falsche I²C-Adresse | `print(i2c.scan())` → gemeldete Adresse in `SSD1306_I2C(..., addr=0x??)` eintragen |
| `ImportError: no module named ssd1306` | Bibliothek fehlt | `lib/ssd1306.py` auf den Pico kopieren |
| DHT11 liefert `OSError` | Zu häufige Abfrage | Warte mindestens 2 s zwischen `sensor.measure()` |
| Sensor reagiert gar nicht | Signal/VCC vertauscht | DHT11-Pinbelegung prüfen (am Modul beschriftet) |
| OLED zeigt "Müll" | Display flackert, Versorgung wackelt | VCC direkt auf 3V3 (nicht über Poti/Sensor) |
