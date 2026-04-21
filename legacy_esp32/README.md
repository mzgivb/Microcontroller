# Legacy · Arduino Nano ESP32

In diesem Ordner liegen die ursprünglichen Skripte aus der ESP32-Phase des
Kurses. Sie werden für die Projektwoche **nicht** mehr verwendet – bleiben
aber zur Referenz und zur Wiederverwendung auf einem ESP32-Board erhalten.

Die Skripte sind **nicht** für den Raspberry Pi Pico H geschrieben (andere
Pinbelegung!). Wer damit arbeiten will, braucht:

- Arduino Nano ESP32 (oder kompatibel)
- MicroPython für ESP32 (nicht für RP2040!)
- die passenden Bibliotheken (`i2c_lcd.py`, `lcd_api.py` aus `../lib/` …)

## Inhalt

| Datei | Zweck |
|-------|-------|
| `interne_led_blinken_lassen.py` | On-Board-LED bei ESP32 (Pin 2) |
| `externe_led_blinken_lassen.py` | Externe LED |
| `externe_led_per_taster.py` | LED + Taster |
| `led_dauerhaft_mit_taster.py` | Taster toggelt LED |
| `led_mit_taster_0_1.py` | Einfachster Taster-Check |
| `mehrere_led_dauerhaft_mit_taster.py` | Mehrere LEDs |
| `poti_auslesen.py` | Potentiometer am ADC |
| `Display_Hallo_Welt.py` / `Display_test.py` | OLED-Tests |
| `display_LCD16_2_Hallo_Welt.py` / `display_LCD16_2_DHT11.py` | LCD 16×2 |
| `Stoppuhr_mit_Display.py` / `Stoppuhr_ohne_Display.py` | Stoppuhr |
| `phyphox_esp32.py` / `DHT11_phyphox_esp32.py` | Phyphox-BLE-Integration |
| `wlan_verbinden.py` | WLAN-Grundverbindung |
