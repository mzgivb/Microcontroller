from machine import I2C, Pin
from machine_i2c_lcd import I2cLcd

# I2C initialisieren
i2c = I2C(0, scl=Pin(22), sda=Pin(21), freq=400000)

# Die richtige I2C-Adresse einstellen (nach Scan)
I2C_ADDR = 0x3F  # Beispieladresse, ersetze durch die tatsächliche Adresse

# LCD initialisieren (16x2 Display)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# Text anzeigen
lcd.putstr("Hallo Welt!")