from machine import Pin
from time import sleep

led1=Pin(12, Pin.OUT)
led2=Pin(13, Pin.OUT)
led3=Pin(14, Pin.OUT)
led4=Pin(15, Pin.OUT)

def test():
    led1.value(1)
    led2.value(1)
    led3.value(1)
    led4.value(1)
    sleep(4)
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)

def turnAllOff():
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(0)

def n1():
    led1.value(1)
    sleep(1)
    led1.value(0)
def n2():
    led2.value(1)
    sleep(1)
    led2.value(0)
def n3():
    led1.value(1)
    led2.value(1)
    sleep(1)
    led1.value(0)
    led2.value(0)
def n4():
    led3.value(1)
    sleep(1)
    led3.value(0)
def n5():
    led1.value(1)
    led3.value(1)
    sleep(1)
def n6():
    led2.value(1)
    led3.value(1)
    sleep(1)
def n7():
    led1.value(1)
    led2.value(1)
    led3.value(1)
    sleep(1)

def n8():
    led4.value(1)
    sleep(1)

def n9():
    led1.value(1)
    led4.value(1)
    sleep(1)

def n10():
    led2(1)
    led4(1)
    sleep(1)

def n11():
    led1(1)
    led2(1)
    led4(1)
    sleep(1)

def n12():
    led3(1)
    led4(1)
    sleep(1)

def n13():
    led1(1)
    led3(1)
    led4(1)
    sleep(1)

def n14():
    led2(1)
    led3(1)
    led4(1)
    sleep(1)

def n15():
    led1(1)
    led2(1)
    led3(1)
    led4(1)
    sleep(1)


    




n1()
turnAllOff()
n2()
turnAllOff()
n3()
turnAllOff()
n4()
turnAllOff()
n5()
turnAllOff()
n6()
turnAllOff()
n7()
turnAllOff()
n8()
turnAllOff()
n9()
turnAllOff()
n10()
turnAllOff()
n11()
turnAllOff()
n12()
turnAllOff()
n13()
turnAllOff()
n14()
turnAllOff()
n15()
turnAllOff()

n15()
turnAllOff()
sleep(0.5)
n15()
turnAllOff()
sleep(0.5)
turnAllOff()
n15()
turnAllOff()
sleep(0.5)
n15()
turnAllOff()
sleep(0.5)
n1()
turnAllOff()
n2()
turnAllOff()
n4()
turnAllOff()
n8()
turnAllOff()
n8()
turnAllOff()
n4()
turnAllOff()
n2()
turnAllOff()
n1()