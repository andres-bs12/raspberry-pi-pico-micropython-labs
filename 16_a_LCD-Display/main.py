import utime as time

try:
    from lcd1602 import LCD
except ImportError:
    print("Pico not found")
    raise

lcd = LCD()
lcd.write(0,0,'hello workld')
while True :
    myName = input('What is your nane?')
    greeting = 'Hello ' + myName
    greeting2 = 'Welcome to my Pi'
    lcd.write(0,0, greeting)
    lcd.write(0,1,greeting2)

