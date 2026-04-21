# Leitfaden für Lehrkräfte

Dieses Dokument hilft Lehrkräften, die Projektwoche Mikrocontroller
vorzubereiten und während der Woche souverän zu begleiten.

---

## 1 · Vorbereitung vor der Woche

### 1.1 · Einmal selbst durchlaufen (Pflicht, ca. 4–6 h)

Arbeite vor der Projektwoche **alle sieben Lektionen** einmal selbst durch. Das
ist die beste Vorbereitung – du kennst dann:

- typische Fehlerquellen (Pin verwechselt, I²C-Adresse falsch, Vorwiderstand
  vergessen),
- die tatsächliche Laufzeit pro Lektion,
- die Stellen, an denen Lernende erfahrungsgemäß hängen bleiben.

### 1.2 · Hardware-Checkliste pro Arbeitsplatz

Siehe [HARDWARE.md](HARDWARE.md). Vor der Woche einmal **vollständig
zusammenstellen** und in einer beschrifteten Box ablegen (z.B. Plastikbox mit
Fächern).

### 1.3 · Software-Checkliste pro Rechner

- [ ] **Thonny** installiert (≥ 4.1) → siehe [SETUP.md](SETUP.md)
- [ ] MicroPython auf Pico H geflasht (UF2-Datei)
- [ ] Bibliotheken aus [`lib/`](lib/) auf den Pico kopiert
- [ ] USB-Kabel (Daten, **nicht** nur Ladekabel!)
- [ ] Rechte: Schüler-Accounts dürfen USB-Geräte nutzen

### 1.4 · Einmal flashen – Vorlage auf allen Picos

Spart viel Zeit in der ersten Stunde: **fertig geflashten + bibliotheksversehenen
Pico** aus einem Master-Pico kopieren. Alternativ Schritt in Lektion 00 der
Schüler:innen aufnehmen.

---

## 2 · Tagesplan 5-Tage-Projektwoche

| Tag | Block 1 (90 min) | Block 2 (90 min) |
|-----|------------------|------------------|
| **Mo** | Begrüßung, Setup (siehe SETUP.md), Lektion 01 – LEDs | Lektion 02 – Taster & Poti |
| **Di** | Lektion 03 – Buzzer & OLED | Lektion 04 – Sensoren (Licht, DHT11) |
| **Mi** | Projekt 05 – Wetterstation (Aufbau) | Projekt 05 – Wetterstation (Erweiterung + Gehäuse) |
| **Do** | Projekt 06 – Süßigkeitenalarm (Aufbau) | Lektion 07 – Brainstorming Eigenes Projekt + Gruppenbildung |
| **Fr** | Lektion 07 – Eigenes Projekt bauen | Präsentationen + Aufräumen |

Die Progression ist so gewählt, dass nach Lektion 04 **alle Bausteine** für die
beiden Projekte bekannt sind. Wer schneller ist, erweitert mit den
**Aufgaben-Blöcken** am Ende jeder Datei.

---

## 3 · Typische Stolperfallen

| Problem | Ursache | Lösung |
|---------|---------|--------|
| Thonny findet den Pico nicht | Ladekabel statt Datenkabel | USB-Kabel tauschen |
| `ImportError: no module named 'ssd1306'` | Bibliothek fehlt auf dem Pico | Datei aus [`lib/`](lib/) auf den Pico kopieren |
| OLED bleibt schwarz | Falsche I²C-Adresse (0x3C vs. 0x3D) | `i2c.scan()` ausführen, ausgegebene Zahl verwenden |
| Taster reagiert „chaotisch" | Prellen | Im Code `sleep(0.05)` nach Erkennung – oder Entprell-Logik |
| DHT11 gibt Fehler bei jeder 2. Messung | Zu schnelle Abfrage | Mindestens 2 s zwischen `sensor.measure()` |
| LED leuchtet schwach | 3V3 statt 5V am OLED – oder Vorwiderstand zu groß | Vorwiderstand 220 Ω verwenden |
| Skript läuft nicht beim Einstecken des Pico | Datei heißt nicht `main.py` | In Thonny "Save as… → Raspberry Pi Pico → main.py" |

---

## 4 · Differenzierung

Jede Lektion hat im unteren Bereich einen Block `AUFGABEN ZUM AUSPROBIEREN`.
Diese sind bewusst gestuft:

- **Aufgabe 1–2:** Bestätigen das Verständnis (schaffen alle)
- **Aufgabe 3:** Fordert Transfer (mittleres Niveau)
- **Aufgabe 4 / „Challenge":** Für schnelle Gruppen / zur Weiterarbeit zu Hause

Mindestziel pro Lektion = Code läuft + Aufgabe 1 gelöst.

---

## 5 · Bewertung (optional)

Wenn eine Leistungsnote vergeben werden soll, empfiehlt sich eine Bewertung des
**eigenen Projekts** (Lektion 07) mit diesen Kriterien:

- Konzept / Idee (20 %)
- Funktion / technische Umsetzung (40 %)
- Code-Qualität & Kommentierung (20 %)
- Präsentation (20 %)

---

## 6 · Anpassung auf andere Formate

- **Doppelstunde über mehrere Wochen:** Lektionen 01–04 einzeln; Projekt als
  Semesterabschluss
- **Tages-Workshop (6 h):** Setup + Lektion 01–03 + Projekt Alarmanlage
- **AG (90 min/Woche):** Eine Lektion pro Termin, Projekte als Abschluss
