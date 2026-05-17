from machine import Pin
import utime as time ## Micro time
from dht import DHT11
from lcd1602 import LCD ## Lcd settings
lcd = LCD()
lcd.write(0,0, 'LCD OK')
lcd.write(0,1, 'Init sensor...')
time.sleep(1)
lcd.clear()

# dht set up
DHT_pin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
myDHT11 = DHT11(DHT_pin)

# Button set up
butpin = 15
myButton = Pin(butpin, Pin.IN, Pin.PULL_UP)
tempUnitC = True
buttonState = 1
buttonStateOld = 1
print('My sensor Data')



while(True):
    buttonState = myButton.value()
    if buttonState == 1 and buttonStateOld == 0:
        tempUnitC = not tempUnitC

    try:
        myDHT11.measure()
    except:
        print("Sensor measure failed")
        buttonStateOld = buttonState
        time.sleep(1)
        continue

    tempC = myDHT11.temperature()
    tempF = tempC * 1.8 + 32 
    hum = myDHT11.humidity()

    print("Temp C:", tempC, "Temp F:", tempF, "Humidity:", hum, end='\r')

    lcd.clear()
    if tempUnitC:
        print("\r", "Temp = ", tempC, chr(176), "C" , ", Humidity = " , hum , " %", end='') # \r overwrite
        lcd.write(0,0, 'Temp: ' + str(tempC) + "\xDF" + "C")
    else:
        print("\r", "Temp = ", tempF, chr(176), "F" , ", Humidity = " , hum , " %", end='') # \r overwrite
        lcd.write(0,0, 'Temp: ' + str(tempF) + "\xDF" + "F")
    lcd.write(0,1, 'Hum: ' + str(hum) + '%')

    time.sleep(1)
    buttonStateOld = buttonState
