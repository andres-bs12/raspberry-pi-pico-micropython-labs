from machine import Pin
from time import sleep

myLed = Pin('LED', Pin.OUT)

while (True):
    myLed.value(0)
    sleep(.04)
    myLed(1)   