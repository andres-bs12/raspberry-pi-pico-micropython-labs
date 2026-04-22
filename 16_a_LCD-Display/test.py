import machine
i2c = machine.I2C(1, sda=machine.Pin(6), scl=machine.Pin(7))
print("Scanning I2C bus...")
devices = i2c.scan()
if len(devices) == 0:
    print("Check physical pins 9 and 10!")
else:
    print("Found device at address:", [hex(d) for d in devices])