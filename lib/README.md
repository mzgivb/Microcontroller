# Bibliotheken

Diese Dateien müssen **auf den Pico** kopiert werden (nicht nur ins Projekt-
Verzeichnis am PC).

In Thonny: Datei öffnen → Rechtsklick → **„Auf /"-Speicher hochladen"**.

| Datei | Wofür? | Ab Lektion |
|-------|--------|------------|
| `ssd1306.py` | OLED-Display SSD1306 (I²C) | 03 |
| `i2c_lcd.py` + `lcd_api.py` | LCD 16×2 mit I²C-Adapter (Alternative zum OLED) | Bonus |
| `machine_i2c_lcd.py` | ältere Variante von `i2c_lcd` | Bonus |

`ssd1306.py` stammt aus [`micropython-lib`](https://github.com/micropython/micropython-lib)
(MIT-Lizenz). Die LCD-Bibliotheken sind Community-Versionen; Quelle siehe Kopfzeile.

## Mit `mip` nachinstallieren (Pico W + WLAN)

Alternativ können die Bibliotheken direkt vom Pico aus aus dem Netz gezogen werden:

```python
import mip
mip.install("ssd1306")
```

(funktioniert nur mit Pico **W** im WLAN)
