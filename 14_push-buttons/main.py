from machine import Pin
from time import sleep

buttonPin = 14

myButton = Pin(buttonPin, Pin.IN, Pin.PULL_UP) # From where, in or out, what action

# Pressed should read 1, when not 0
while True:
    buttonState = myButton.value() # reads whethe rthe button is pressed or not
    print(buttonState)
    sleep(.1)

