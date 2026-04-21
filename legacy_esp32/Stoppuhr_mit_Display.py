from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd
import time

# I2C und LCD initialisieren
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)
I2C_ADDR = 0x3F  # Anpassen, falls nötig
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)  # 2 Zeilen, 16 Spalten

# Taster-Pin (mit internem Pull-up)
start_button = Pin(15, Pin.IN, Pin.PULL_UP)

running = False
start_time = 0
elapsed = 0

def update_display(elapsed_ms):
    # Umrechnung in Sekunden, Millisekunden
    sec = elapsed_ms // 1000
    ms = elapsed_ms % 1000
    lcd.clear()
    lcd.putstr("Zeit:")
    lcd.move_to(0,1)
    lcd.putstr("{:02d}.{:03d} s".format(sec, ms))

# Anfangsanzeige
lcd.clear()
lcd.putstr("Stoppuhr bereit")
time.sleep(2)
lcd.clear()

prev_button_state = start_button.value()

while True:
    current_button_state = start_button.value()
    
    # Beim Fallen von HIGH auf LOW starten/stoppen
    if prev_button_state == 1 and current_button_state == 0:
        if running:
            # Stopp
            elapsed = time.ticks_diff(time.ticks_ms(), start_time)
            running = False
        else:
            # Start
            start_time = time.ticks_ms()
            running = True

    prev_button_state = current_button_state

    # Wenn läuft, Zeit aktualisieren
    if running:
        current_elapsed = time.ticks_diff(time.ticks_ms(), start_time)
        update_display(current_elapsed)
    else:
        # Anzeige hält letzte Zeit
        update_display(elapsed)

    time.sleep_ms(100)  # leichte Verzögerung, um Display nicht zu flackern