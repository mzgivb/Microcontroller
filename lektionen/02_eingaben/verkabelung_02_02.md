# Verkabelung · Lektion 02.02 · Taster + LED

```
 Pico H                          Breadboard
 ┌──────────────────┐
 │ GPIO14 (Pin 19) ─┼───── Taster ───── GND (Pin 18)
 │                  │
 │ GPIO15 (Pin 20) ─┼───── [220 Ω] ──── LED Anode
 │                  │                      │
 │                  │                     LED Kathode
 │     GND (Pin 23)─┼──────────────────────
 └──────────────────┘
```

## Bauteile

- 1× Taster (Mikroschalter, 4 Beine → je zwei sind intern verbunden)
- 1× LED
- 1× 220 Ω Widerstand
- 4 Jumper

## Stolperfallen

- Taster hat 4 Beine, aber zwei davon sind direkt verbunden. Steckt ihn quer
  über die Mittenlücke des Breadboards, dann seid ihr auf der sicheren Seite.
- Den Pull-Up-Widerstand macht der Pico intern – keine externe Beschaltung
  nötig.
