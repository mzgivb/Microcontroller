import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("ssid", "xxxxxxxx")

while not wlan.isconnected():
    pass

print("Verbunden, IP-Adresse:", wlan.ifconfig()[0])
