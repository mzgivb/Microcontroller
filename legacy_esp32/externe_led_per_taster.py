from machine import Pin

# LED und Button konfigurieren am Arduino NANOESP32
led = Pin(5, Pin.OUT) # D2
button = Pin(7, Pin.IN, Pin.PULL_UP) # D4

while True:
    if button.value() == 0:  # Taster gedrückt
        led.value(1)         # LED einschalten
    else:                    # Taster nicht gedrückt
        led.value(0)         # LED ausschalten

        
        
    

 





