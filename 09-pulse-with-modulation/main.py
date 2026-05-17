from time import sleep
from machine import PWM,Pin

outPin = 16

analogOut=PWM(Pin(outPin))
analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
    myVoltage = float(input('What Voltage do you want'))
    pwmVal = (65375/3.3) * myVoltage
    analogOut.duty_u16(int(pwmVal))
    sleep(.1)
    