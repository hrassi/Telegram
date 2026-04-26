from wifi_connect import wifi_loop
from telegram import send_telegram
from machine import Pin
from machine import WDT
import time



MyNetwork = "Rassi Net3"
MyPassword = "Holyshit"

DEVICE_ID = "ESP77"  # change per device

boot_btn = Pin(0, Pin.IN, Pin.PULL_UP)


# ───── 1. WAIT FOR WIFI AT STARTUP ─────
print("[System] Connecting to WiFi...")

while not wifi_loop(MyNetwork, MyPassword):
    time.sleep_ms(500)
print("[System] WiFi connected!")
send_telegram(DEVICE_ID, "first connection done")



wdt = WDT(timeout=30000)  # 30 seconds



while True:
    wifi_loop(MyNetwork, MyPassword)
    
    
    if not boot_btn.value():   # pressed (LOW)
        print("BOOT button pressed")
        send_telegram(DEVICE_ID, "message from main loop")
         
    # Your system runs freely here (MQTT, sensors, UI, etc.)
    wdt.feed()           # reset watchdog timer
    time.sleep_ms(100)
    




   