import machine 


from time import sleep

ledRed = machine.Pin(15, machine.Pin.OUT)
ledYellow = machine.Pin(14, machine.Pin.OUT)
ledGreen = machine.Pin(13, machine.Pin.OUT)
potPin = 28
myPot = machine.ADC(potPin)

while(True) :
        potVal = myPot.read_u16() # This is the pontenciometer
    
        voltage = (100/65375) * potVal - (160 * 100 / 65375)
        sleep(.5)
        if voltage <= 5:
                ledRed.value(0)
                ledYellow.value(0)
                ledGreen.value(0)

        if voltage >= 6 and voltage < 36:
            ledRed.value(1)
            ledYellow.value(0)
            ledGreen.value(0)

        if voltage >= 36 and voltage < 70:
            ledRed.value(0)
            ledYellow.value(1)
            ledGreen.value(0)

        if voltage  >= 70:
            ledRed.value(0)
            ledYellow.value(0)
            ledGreen.value(1)

