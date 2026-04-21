# Verkabelung · Lektion 01.03 · Externe LED

```
 Pico H                         Breadboard
 ┌──────────────────┐
 │                  │
 │ GPIO15 (Pin 20) ─┼───┬──── [220 Ω] ──── (Anode, langes Bein)
 │                  │                           │
 │                  │                          LED
 │                  │                           │
 │                  │              (Kathode, kurzes Bein)
 │    GND (Pin 23) ─┼───┴─────────────────────
 │                  │
 └──────────────────┘
```

## Bauteile

| Stück | Bauteil |
|-------|---------|
| 1× | LED 5 mm (beliebige Farbe) |
| 1× | Widerstand **220 Ω** (Farbringe: rot-rot-braun oder orange-orange-braun) |
| 2× | Jumperkabel Male-Male |

## Schrittfolge

1. Pico vom USB trennen (immer erst spannungsfrei bauen!).
2. Pico auf das Breadboard stecken (USB-Port zeigt nach außen).
3. Widerstand in eine freie Reihe stecken.
4. LED: **langes Bein** an das eine Ende des Widerstands, **kurzes Bein** in
   eine andere Reihe.
5. Jumper-Kabel von `GPIO 15` (Pin 20) zum anderen Ende des Widerstands.
6. Jumper-Kabel vom kurzen LED-Bein zu `GND` (Pin 23).
7. Pico wieder per USB anschließen und Skript starten.

## Wenn's nicht leuchtet

- LED andersherum stecken (Polung).
- Widerstand richtig? (220 Ω, nicht 10 kΩ!)
- Richtiger GPIO-Pin im Code und im Kabel?
- Kontakt auf dem Breadboard (LED/Widerstand richtig gesteckt)?
