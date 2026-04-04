from machine import Pin
from time import sleep


redLed = Pin(15 ,Pin.OUT)

def makeS():
    redLed.value(1)
    sleep(1)
    redLed.value(0)
    sleep(1)
    redLed.value(1)
    sleep(1)
    redLed.value(0)
    sleep(1)
    redLed.value(1)
    sleep(1)


def waitTime():
    sleep(3)


def makeO():
    redLed.value(0)
    sleep(1)
    redLed.value(1)
    sleep(3)
    redLed.value(0)
    sleep(1)
    redLed.value(1)
    sleep(3)
    redLed.value(0)

while (True):
    makeS()
    waitTime()
    makeO()



