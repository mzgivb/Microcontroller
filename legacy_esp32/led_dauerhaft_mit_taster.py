from machine import Pin
import time

led = Pin(5, Pin.OUT)         # LED an Pin 5
button = Pin(7, Pin.IN, Pin.PULL_UP)  # Taster an Pin 7 mit internem Pull-Up

led_state = False             # Aktueller LED-Zustand (False = aus, True = an)
button_prev = button.value()  # Vorheriger Tasterwert

while True:
    button_state = button.value()
    # Wenn der Taster gerade gedrückt wurde (Übergang von High zu Low)
    if button_prev == 1 and button_state == 0:
        led_state = not led_state  # LED-Zustand umschalten
        led.value(led_state)        # LED entsprechend setzen
        time.sleep(0.2)             # Kurze Pause für Debouncing
    button_prev = button_state
    time.sleep(0.01)
