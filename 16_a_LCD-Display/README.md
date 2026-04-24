# Lesson 16A - LCD Display (I2C)

## Status
Working. Finally.

## What Happened (aka "I bought another LCD to be able to continue the lesson, but it turned out I just had a wiring issue")
This lesson was supposed to be easy: connect LCD1602, print text, feel like a hardware genius.

Reality: `i2c.scan()` returned `[]` every time, I thought the module was dead, and yes, I bought a second LCD.

Actual root cause: the Raspberry Pi Pico was shifted by one pin on the breadboard.
So the wiring looked right... but was wrong.

After fixing the board alignment and reconnecting everything, I2C started working.

So no, the first module was not dead. My alignment was.

## Files In This Lesson
- `lcd1602.py`: LCD I2C driver (common addresses: `0x27`, `0x3F`)
- `main.py`: simple hello-world example
- `test.py`: full diagnostic test to detect wiring, bus, or module issues fast

## Wiring Used In This Project
- SDA -> GP6
- SCL -> GP7
- GND -> any GND pin (example: physical pin 38)
- VCC -> 3V3 for safe testing (or 5V only if you know your logic levels are OK)

## How To Use `test.py`
Upload `test.py` to your Pico and run it from the MicroPython REPL.

It runs this sequence:
1. `TEST 0`: checks SDA/SCL electrical idle state
2. `SCAN`: hardware I2C scan at 100 kHz and 400 kHz (GP6/GP7)
3. `SCAN SOFT`: SoftI2C fallback scan at lower speeds
4. `SCAN EXTRA`: scans other valid Pico I2C pin pairs
5. `TEST 1`: raw backlight blink test (direct write to backpack)
6. `TEST 2`: text patterns + simple animation
7. `QUICK DIAGNOSIS`: short summary of what likely failed

## Reading The Results Quickly
- All scans empty:
  wiring issue, shifted board, bad jumper, or dead backpack.
- Backlight works but no text:
  likely contrast/backpack mapping/init issue.
- Text + animation show correctly:
  module and wiring are good.
- SDA or SCL is `0` in `TEST 0`:
  bus may be shorted or held low.

## Lessons Learned
- Check Pico alignment on the breadboard before touching code.
- Verify by pin labels and physical pin numbers, not by "looks right".
- Run I2C scan first, panic later.
- Buying a spare module is fine.
- Buying a spare module because of one-pin misalignment is... character development.
