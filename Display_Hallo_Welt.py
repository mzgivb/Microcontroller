from machine import I2C, Pin
from i2c_lcd import I2cLcd

# I2C initialisieren
i2c = I2C(0, scl=Pin(12), sda=Pin(11), freq=400000)

# Die richtige I2C-Adresse einstellen (nach Scan)
I2C_ADDR = 0x3f  # Beispieladresse, ersetze durch die tatsächliche Adresse

# LCD initialisieren (16x2 Display)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)
lcd.clear()  # Bildschirm löschen
lcd.backlight_on()  # Hintergrundbeleuchtung einschalten
lcd.putstr("Neustart läuft...")  # Nachricht anzeigen
# Text anzeigen
lcd.putstr("Hallo Welt!")