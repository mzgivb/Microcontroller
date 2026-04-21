from machine import I2C, Pin
from i2c_lcd import I2cLcd


import time

# I2C initialisieren
i2c = I2C(0, scl=Pin(12), sda=Pin(11), freq=400000) #VBUS nutzen statt 3V

# LCD initialisieren (16x2 Display)
I2C_ADDR = 0x3F  # Verwende die tatsächliche Adresse
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)  # 2 Zeilen, 16 Zeichen

lcd.clear()   # Bildschirm löschen und Text anzeigen      
lcd.putstr("Hallo Welt")


