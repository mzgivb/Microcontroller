from machine import ADC, Pin
import time

adc = ADC(Pin(34))  # Pin anpassen
adc.width(ADC.WIDTH_10BIT)   # 10 Bit Auflösung
adc.atten(ADC.ATTN_11DB)     # Messbereich erweitern

while True:
    wert = adc.read()
    print("ADC-Wert:", wert)
    time.sleep(0.5)