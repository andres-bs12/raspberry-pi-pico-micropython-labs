import machine
import utime as time

try:
    from lcd1602 import LCD
except ImportError:
    print("Failed to import lcd1602.py")
    raise


# Project base settings
I2C_ID = 1
SDA_PIN = 6
SCL_PIN = 7
FREQUENCIES = (100000, 400000)

# Valid I2C pin pairs for Raspberry Pi Pico/Pico 2
FALLBACK_I2C_PAIRS = {
    0: ((0, 1), (4, 5), (8, 9), (12, 13), (16, 17), (20, 21)),
    1: ((2, 3), (6, 7), (10, 11), (14, 15), (18, 19), (26, 27)),
}


def scan_i2c(freq):
    i2c = machine.I2C(I2C_ID, sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=freq)
    devices = i2c.scan()
    print("\n[SCAN] Frequency:", freq, "Hz")
    if devices:
        print("[SCAN] Devices found:", [hex(d) for d in devices])
    else:
        print("[SCAN] No I2C devices detected")
    return i2c, devices


def fallback_scan_all_i2c(freq=100000):
    print("\n[SCAN EXTRA] Scanning alternative I2C pin pairs")
    found = []
    for bus_id, pairs in FALLBACK_I2C_PAIRS.items():
        for sda_pin, scl_pin in pairs:
            try:
                i2c = machine.I2C(
                    bus_id,
                    sda=machine.Pin(sda_pin),
                    scl=machine.Pin(scl_pin),
                    freq=freq,
                )
                devices = i2c.scan()
                if devices:
                    print(
                        "[SCAN EXTRA] Bus",
                        bus_id,
                        "SDA=GP" + str(sda_pin),
                        "SCL=GP" + str(scl_pin),
                        "->",
                        [hex(d) for d in devices],
                    )
                    found.append((bus_id, sda_pin, scl_pin, devices))
            except Exception:
                pass
    if not found:
        print("[SCAN EXTRA] No response on any valid I2C pair")
    return found


def line_state_test(sda_pin=SDA_PIN, scl_pin=SCL_PIN):
    print("\n[TEST 0] Electrical line state of I2C")
    sda = machine.Pin(sda_pin, machine.Pin.IN, machine.Pin.PULL_UP)
    scl = machine.Pin(scl_pin, machine.Pin.IN, machine.Pin.PULL_UP)
    sda_v = sda.value()
    scl_v = scl.value()
    print("[TEST 0] SDA=", sda_v, "SCL=", scl_v)
    print("[TEST 0] Expected at idle: SDA=1 and SCL=1")

    if sda_v == 0 or scl_v == 0:
        print("[TEST 0] ALERT: one line is at 0 (short to GND or module blocking bus)")
        print("[TEST 0] Disconnect LCD and re-run this test")
    else:
        print("[TEST 0] Lines high: no obvious short")


def soft_i2c_scan(sda_pin=SDA_PIN, scl_pin=SCL_PIN):
    print("\n[SCAN SOFT] SoftI2C scan on GP" + str(sda_pin) + "/GP" + str(scl_pin))
    found_any = []
    for f in (10000, 50000, 100000):
        try:
            i2c = machine.SoftI2C(sda=machine.Pin(sda_pin), scl=machine.Pin(scl_pin), freq=f)
            devices = i2c.scan()
            if devices:
                print("[SCAN SOFT]", f, "Hz ->", [hex(d) for d in devices])
                for d in devices:
                    if d not in found_any:
                        found_any.append(d)
            else:
                print("[SCAN SOFT]", f, "Hz -> []")
        except Exception as ex:
            print("[SCAN SOFT] Error at", f, "Hz:", ex)
    return found_any


def raw_backlight_test(i2c, addr, cycles=5):
    print("\n[TEST 1] Raw backlight (without LCD library)")
    print("[TEST 1] Address:", hex(addr))
    print("[TEST 1] If backlight blinks, I2C backpack is alive")
    for _ in range(cycles):
        i2c.writeto(addr, bytearray([0x08]))
        time.sleep_ms(250)
        i2c.writeto(addr, bytearray([0x00]))
        time.sleep_ms(250)
    i2c.writeto(addr, bytearray([0x08]))


def text_pattern_test(addr):
    print("\n[TEST 2] Library initialization + text")
    print("[TEST 2] Forced address:", hex(addr))
    lcd = LCD(addr=addr)

    lcd.clear()
    lcd.write(0, 0, "1234567890123456")
    lcd.write(0, 1, "abcdefABCDEF7890")
    print("[TEST 2] Pattern 1 shown for 3s")
    time.sleep(3)

    lcd.clear()
    lcd.write(0, 0, "LINE 1 OK?")
    lcd.write(0, 1, "LINE 2 OK?")
    print("[TEST 2] Pattern 2 shown for 3s")
    time.sleep(3)

    lcd.clear()
    for pos in range(16):
        lcd.clear()
        lcd.write(pos, 0, "*")
        lcd.write(15 - pos, 1, "#")
        time.sleep_ms(160)

    lcd.clear()
    lcd.write(0, 0, "TEST COMPLETED")
    lcd.write(0, 1, "CHECK CONSOLE")


def print_diagnosis(devices_found, text_test_ok):
    print("\n=== QUICK DIAGNOSIS ===")
    if not devices_found:
        print("1) No I2C response: probable backpack failure, wiring, or pin issue.")
        print("2) Check VCC, GND, SDA(GP6), SCL(GP7), and solder joints.")
        return

    if text_test_ok:
        print("1) I2C response detected and library successfully wrote.")
        print("2) If you saw text/animation, LCD is working correctly.")
        print("3) If no display, adjust contrast (blue potentiometer) and check backlight.")
    else:
        print("1) I2C response detected, but text initialization/write failed.")
        print("2) Possible backpack incompatibility or LCD control circuit damage.")


def main():
    print("=== LCD1602 TEST TO RULE OUT FAILURE ===")
    print("Pins used: SDA=GP6, SCL=GP7, Bus=I2C1")

    line_state_test()

    all_devices = []
    i2c_ref = None
    for freq in FREQUENCIES:
        i2c_ref, devices = scan_i2c(freq)
        for d in devices:
            if d not in all_devices:
                all_devices.append(d)

    if not all_devices:
        soft_devices = soft_i2c_scan()
        if soft_devices:
            print("\n[INFO] SoftI2C detected device(s):", [hex(d) for d in soft_devices])
            print("[INFO] Use SoftI2C for this module or check I2C hardware mapping.")
            print_diagnosis(True, False)
            return

        fallback_hits = fallback_scan_all_i2c()
        if fallback_hits:
            print("\n[INFO] I2C detected on pins other than GP6/GP7.")
            print("[INFO] Check wiring and adjust SDA/SCL to correct pair.")
        print_diagnosis(False, False)
        return

    # Usually 0x27 or 0x3F; if not, use first detected.
    if 0x27 in all_devices:
        target_addr = 0x27
    elif 0x3F in all_devices:
        target_addr = 0x3F
    else:
        target_addr = all_devices[0]

    raw_backlight_test(i2c_ref, target_addr)

    text_ok = False
    try:
        text_pattern_test(target_addr)
        text_ok = True
    except Exception as ex:
        print("[ERROR] Text test failed:", ex)

    print_diagnosis(True, text_ok)


main()