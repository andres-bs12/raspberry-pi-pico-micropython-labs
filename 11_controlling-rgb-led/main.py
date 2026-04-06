from machine import Pin, PWM
from time import sleep


redPin = 13
greenPin = 14
bluePin = 15

redLED = PWM(Pin(redPin))
greenLED = PWM(Pin(greenPin))
bluenLED = PWM(Pin(bluePin))

redLED.freq(1000)
redLED.duty_u16(0)

greenLED.freq(1000)
greenLED.duty_u16(0)

bluenLED.freq(1000)
bluenLED.duty_u16(0)
 
 # Have to ask wich color does the user wants (Red, Green blue, cient, magent, yellow, orange, white)
 # Have to create a stop 
 # have to create a turn off

while(True):
    redBright = 0
    greenBright = 0
    blueBright = 0
    color = input("Wich color do you want?").strip().lower()

    if (color == "none"):
        redBright = 0
        greenBright = 0
        blueBright = 0
        redLED.duty_u16(redBright)
        greenLED.duty_u16(greenBright)
        bluenLED.duty_u16(blueBright)
        continue

    elif (color == "red"):
        redBright = 65500
        greenBright = 0
        blueBright = 0

    elif (color == "green"):
        redBright = 0
        greenBright = 65500
        blueBright = 0

    elif (color == "blue"):
        redBright = 0
        greenBright =0
        blueBright = 65500

    elif (color == "cian"):
        redBright = 0
        greenBright = 65500
        blueBright = 65500

    elif (color == "magneta"):
        redBright = 65500
        greenBright = 0
        blueBright = 65500

    elif (color == "yellow"):
        redBright = 65500
        greenBright = 65500
        blueBright = 0

    elif (color == "orange"):
        redBright = 65500
        greenBright = 7000
        blueBright = 0

    


    redLED.duty_u16(redBright)
    greenLED.duty_u16(greenBright)
    bluenLED.duty_u16(blueBright)

    sleep(.2)






