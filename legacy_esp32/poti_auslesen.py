from machine import ADC, Pin
import time

adc = ADC(Pin(12))  # Pin anpassen
  
adc.atten(ADC.ATTN_11DB) # Messbereich erweitern
adc.width(ADC.WIDTH_12BIT) # 12 Bit Auflösung

while True:
    wert = (adc.read() /4)
    print("ADC-Wert:", wert)
    time.sleep(0.5)