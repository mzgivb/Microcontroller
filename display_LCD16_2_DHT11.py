from machine import I2C, Pin
from i2c_lcd import I2cLcd
import dht
import time

# I2C initialisieren
i2c = I2C(0, scl=Pin(12), sda=Pin(11), freq=400000) #VBUS nutzen statt 3V

# LCD initialisieren (16x2 Display)
I2C_ADDR = 0x3F  # Verwende die tatsächliche Adresse
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)  # 2 Zeilen, 16 Zeichen
dht_pin = Pin(8,Pin.OUT)
sensor = dht.DHT11(dht_pin)
def main():
      while True:
         try:
            sensor.measure()
            humidity = sensor.humidity()               #Send value to phyphox
            time.sleep_ms(500)  #Shortly pause before repeating
            lcd.clear()   # Bildschirm löschen und Text anzeigen      
            lcd.putstr(f"Luftfeuchtigkeit: {humidity}%")
            print(f"Luftfeuchtigkeit: {humidity}%")
         except OSError as e:
            print("Fehler beim Auslesen des DHT11:", e)
         time.sleep(2)  # Wartezeit zwischen Messungen
main()



