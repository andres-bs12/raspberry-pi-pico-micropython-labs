from machine import Pin
from time import sleep

buttonPin = 14
led1=Pin(17, Pin.OUT)

myButton = Pin(buttonPin, Pin.IN, Pin.PULL_UP) # From where, in or out, what action


ledState = 0
led1.value(ledState)
lastButtonState = myButton.value()


# Pressed should read 1, when not 0
while True:
    buttonState = myButton.value() # reads whethe rthe button is pressed or not

    if lastButtonState == 0 and buttonState == 1: # if button was not pressed and now it is
        ledState = not ledState # Whetever is now change to the the another
        led1.value(ledState)
        sleep(.1)
    
    lastButtonState = buttonState
    sleep(.1)

# 330 resistor
# on off switch 