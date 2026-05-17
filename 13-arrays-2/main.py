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


availableColors = ['none', 'red', 'green', 'blue', 'cian', 'magneta', 'yellow', 'orange']
colorsToReproduce = []

while True:
    redBright = 0
    greenBright = 0
    blueBright = 0
    colorsToReproduce = []

    try:
        numBlinks = int(input('How many blinks? '))  # Careful with the int to convert str to int
    except ValueError:
        print('invalid number ')
        continue

    for blink in range(numBlinks):
        while True:
            color = input('What Color ').strip().lower()
            if color in availableColors:
                colorsToReproduce.append(color)
                break
            print('invalid color')

    for color in colorsToReproduce:
        if (color == "none"):
            redBright = 0
            greenBright = 0
            blueBright = 0

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
            greenBright = 0
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
        sleep(0.5)

        redLED.duty_u16(0)
        greenLED.duty_u16(0)
        bluenLED.duty_u16(0)
        sleep(0.2)
                    


# Create the plate with the nice led 
# as how many colors does the user wants to see
# okey wich one has to be. the first color ...
# and then show them 