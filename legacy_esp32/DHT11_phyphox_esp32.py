from phyphoxBLE import PhyphoxBLE, Experiment
import time
from machine import Pin
import dht

dht_pin = Pin(8,Pin.OUT)
sensor = dht.DHT11(dht_pin)

def main():
    p = PhyphoxBLE()
    p.start()
    
    while True:
         try:
            sensor.measure()
            humidity = sensor.humidity()
            p.write(humidity)                #Send value to phyphox
            time.sleep_ms(500)  #Shortly pause before repeating
        
            print(f"Luftfeuchtigkeit: {humidity}%")
         except OSError as e:
            print("Fehler beim Auslesen des DHT11:", e)

         time.sleep(2)  # Wartezeit zwischen Messungen
            
  # Wartezeit zwischen Messungen
main()