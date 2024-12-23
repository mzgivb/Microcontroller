import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("#painthehillgreen", "58635893649059329147")

while not wlan.isconnected():
    pass

print("Verbunden, IP-Adresse:", wlan.ifconfig()[0])