from machine import Pin
import time

# Taster-Pin mit internem Pull-up aktivieren
# Beispiel: Pin 15 als Taster-Eingang
button_pin = Pin(15, Pin.IN, Pin.PULL_UP)

running = False
start_time = 0
elapsed = 0

prev_button_state = button_pin.value()

print("Stoppuhr bereit. Drücke den Taster, um zu starten oder zu stoppen.")

while True:
    current_button_state = button_pin.value()
    
    # Flankenerkennung (von HIGH auf LOW)
    if prev_button_state == 1 and current_button_state == 0:
        if running:
            # Stopp
            elapsed = time.ticks_diff(time.ticks_ms(), start_time)
            running = False
            print("Stoppuhr gestoppt. Zeit: {:.3f} s".format(elapsed / 1000))
        else:
            # Start
            start_time = time.ticks_ms()
            running = True
            print("Stoppuhr gestartet.")
    
    prev_button_state = current_button_state

    # Wenn laufend, kann man optional die aktuelle Zeit anzeigen (optional)
    # Du kannst das einkommentieren, um jede Sekunde ein Update zu sehen
    if running and time.ticks_diff(time.ticks_ms(), start_time) % 1000 < 50:
        current_elapsed = time.ticks_diff(time.ticks_ms(), start_time) / 1000
        print("Aktuelle Zeit: {:.3f} s".format(current_elapsed))

    time.sleep_ms(50)