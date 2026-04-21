# Erweiterungen für die Wetterstation

Wenn das Grundprojekt läuft – hier eine Auswahl von Weiterentwicklungen,
gestaffelt nach Schwierigkeit.

## Leicht

1. **Min/Max-Anzeige:** Merke dir die niedrigste und höchste gemessene
   Temperatur und zeige sie unten auf dem Display an.

2. **Warnton:** Verbinde einen Buzzer (siehe Lektion 03). Wenn die Temperatur
   über 30 °C oder die Feuchte über 70 % steigt, spielt der Buzzer einen Ton.

3. **Balkenanzeige:** Zeichne zwei Balken auf dem OLED – einer für Temperatur,
   einer für Feuchtigkeit. Tipp: `display.fill_rect(x, y, breite, hoehe, 1)`.

## Mittel

4. **Gleitender Mittelwert:** Statt jeder Einzelmessung zeigst du den
   Durchschnitt der letzten 10 Werte (Liste + `sum/len`).

5. **Zeitstempel:** Zeige in der unteren Zeile, wie lange das Gerät läuft
   (in Minuten) – Tipp: `time.ticks_ms()` bei Start merken.

6. **Trend-Pfeil:** Vergleiche den aktuellen mit dem letzten Wert und zeige
   einen Pfeil nach oben / unten / gerade.

## Anspruchsvoll

7. **Logging auf den Pico:** Schreibe alle 10 Minuten die Werte in eine Datei
   `messwerte.csv`. Später kannst du die Datei über Thonny vom Pico ziehen
   und in Excel / Python auswerten.

8. **WLAN-Upload (nur Pico W!):** Sende die Werte an einen Cloud-Dienst
   (z.B. ThingSpeak oder eigenes MQTT) für Live-Graphen.

9. **Gehäuse bauen:** Druckt ein 3D-Gehäuse oder baut eins aus Pappe /
   Holz. Vergesst ein kleines Loch beim DHT11 nicht, sonst misst er sein
   eigenes Gehäuse mit.
