from machine import I2C, Pin
from i2c_lcd import I2cLcd
from time import sleep

# I2C initialisieren
i2c = I2C(0, scl=Pin(12), sda=Pin(11), freq=400000)

# LCD initialisieren (16x2 Display)
lcd = I2cLcd(i2c, 0x3F, 2, 16)  # 0x3F ist die Adresse, passe sie ggf. an

# Begrüßungstext anzeigen
lcd.putstr("Hallo Welt!")
sleep(2)

# Display löschen und dynamische Anzeige
lcd.clear()
for i in range(10):
    lcd.clear()
    lcd.putstr(f"Zahl: {i}")
    sleep(1)

# Abschiedstext
lcd.clear()
lcd.putstr("AufWiedersehen!")