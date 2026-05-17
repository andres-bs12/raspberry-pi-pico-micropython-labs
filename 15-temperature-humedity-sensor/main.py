
from machine import Pin, PWM
from utime import sleep
from dht import DHT11


DHT_pin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
myDHT11 = DHT11(DHT_pin)
myButton = Pin(15, Pin.IN, Pin.OUT)

lastButtonState = myButton.value()
mostrarF = False 

while True:
    myButtonState = myButton.value()

    if myButtonState == 1 and lastButtonState == 0:
        mostrarF = not mostrarF 
        sleep(0.05)

    try:
        myDHT11.measure()
    except:
        sleep(1)
        lastButtonState = myButtonState
        continue

    tempC = myDHT11.temperature()
    tempF = tempC * 1.8 + 32 
    humid = myDHT11.humidity()

    if mostrarF:
        print(f"Temp ={tempF}{chr(117)}F, Humiditi = {humid}%", end="\r")
    else:
        print(f"Temp = {tempC}{chr(176)}C, Humidity = {humid}%", end="\r")

    sleep(1)
    lastButtonState = myButtonState
