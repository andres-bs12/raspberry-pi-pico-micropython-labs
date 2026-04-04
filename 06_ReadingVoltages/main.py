import machine 
from time import sleep

potPin = 28
myPot = machine.ADC(potPin)


while True:
    potVal = myPot.read_u16()
    # voltage = (3.3/65375) * potVal - (160 * 3.3 / 65375) # super important to convert to voltage
    voltage = (100/65375) * potVal - (160 * 100 / 65375)
    print(voltage)
    sleep(.5)

