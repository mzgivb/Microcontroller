from machine import Pin
import time

# Beispiel-Pins (bitte an deine Hardware anpassen)
led_pins = [5, 6,]
button_pins = [7, 8]

# LEDs und Taster konfigurieren
leds = [Pin(pin, Pin.OUT) for pin in led_pins]
buttons = [Pin(pin, Pin.IN, Pin.PULL_UP) for pin in button_pins]

# Aktuelle Zustände der LEDs speichern (False = aus, True = an)
led_state = [False, False, False, False]
# Vorherige Tasterzustände ermitteln
button_prev = [button.value() for button in buttons]

while True:
    for i, button in enumerate(buttons):
        current = button.value()
        # Erkennen des Übergangs von "nicht gedrückt" (High) zu "gedrückt" (Low)
        if button_prev[i] == 1 and current == 0:
            led_state[i] = not led_state[i]
            leds[i].value(led_state[i])
            time.sleep(0.2)  # Debounce-Pause
        button_prev[i] = current
    time.sleep(0.01)
