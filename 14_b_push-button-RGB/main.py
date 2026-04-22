from machine import Pin, PWM
from time import sleep_ms

# Buttons
myButtonGreen = Pin(15, Pin.IN, Pin.PULL_UP)
myButtonYellow = Pin(14, Pin.IN, Pin.PULL_UP)
myButtonRed = Pin(13, Pin.IN, Pin.PULL_UP)
myButtonBlue = Pin(12, Pin.IN, Pin.PULL_UP)

# RGB LED
redLED = PWM(Pin(18))
greenLED = PWM(Pin(17))
blueLED = PWM(Pin(16))

for led in (redLED, greenLED, blueLED):
    led.freq(1000)
    led.duty_u16(0)

redBright = 0
greenBright = 0
blueBright = 0
yellowOn = False

lastRedButtonState = myButtonRed.value()
lastGreenButtonState = myButtonGreen.value()
lastBlueButtonState = myButtonBlue.value()
lastYellowButtonState = myButtonYellow.value()

while True:
    redButtonState = myButtonRed.value()
    greenButtonState = myButtonGreen.value()
    blueButtonState = myButtonBlue.value()
    yellowButtonState = myButtonYellow.value()

    if lastRedButtonState == 1 and redButtonState == 0:
        redBright = 65535 - redBright
        redLED.duty_u16(redBright)
        sleep_ms(30)

    if lastGreenButtonState == 1 and greenButtonState == 0:
        greenBright = 65535 - greenBright
        greenLED.duty_u16(greenBright)
        sleep_ms(30)

    if lastBlueButtonState == 1 and blueButtonState == 0:
        blueBright = 65535 - blueBright
        blueLED.duty_u16(blueBright)
        sleep_ms(30)
        
    if lastYellowButtonState == 1 and yellowButtonState == 0:
        yellowOn = not yellowOn
        if yellowOn:
<<<<<<< HEAD
            redLED.duty_u16(65535) # probar en suma o juntos 
=======
            redLED.duty_u16(65535)
>>>>>>> d85760c63a8c13b64ad924ade7bdda9f9fda6bbe
            greenLED.duty_u16(65535)
        else:
            redLED.duty_u16(0)
            greenLED.duty_u16(0)
        sleep_ms(30)

    lastRedButtonState = redButtonState
    lastGreenButtonState = greenButtonState
    lastBlueButtonState = blueButtonState
    lastYellowButtonState = yellowButtonState

    sleep_ms(10)
