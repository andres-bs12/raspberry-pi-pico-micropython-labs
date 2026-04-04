from machine import Pin
from time import sleep

led1=Pin(12, Pin.OUT)
led2=Pin(13, Pin.OUT)
led3=Pin(14, Pin.OUT)
led4=Pin(15, Pin.OUT)
led5=Pin(11, Pin.OUT)


def t1():
    led1.value(1)
    sleep(.4)
    led1.value(0)
def t2():
    led2.value(1)
    sleep(.4)
    led2.value(0)
def t3():
    led3.value(1)
    sleep(.4)
    led3.value(0)
def t4():
    led4.value(1)
    sleep(.4)
    led4.value(0)
def t5():
    led5.value(1)
    sleep(.5)
    led5.value(0)
def straight():
    t1()
    t2()
    t3()
    t4()
    t5()
    turnAllOff()
def back():
    t5()
    t4()
    t3()
    t2()
    t1()
    turnAllOff()
def turnAllOff():
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)
    led5.value(0)
    
def edges():
    led1.value(1)
    led5.value(1)
    sleep(0.4)
    turnAllOff()
def center():
    t3()
def insideEdges():
    led2.value(1)
    led4.value(1)
    sleep(.4)
    turnAllOff()
def blink():
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    led5.value(1)
    sleep(.4)
    turnAllOff()



turnAllOff()
straight()
turnAllOff()
center()
back()
center()
edges()
center()
insideEdges()
edges()
blink()
edges()
blink()
center()
blink()
insideEdges()
back()
blink()
straight()
blink()
blink()
blink()
center()
insideEdges()
center()
edges()
center()
insideEdges()
center()
edges()
center()
center()
blink()


