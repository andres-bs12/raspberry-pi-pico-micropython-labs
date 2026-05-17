# Lesson 17 - Portable Power + LCD Demo

## Status
Ready / Tested on Pico with LCD1602 (I2C backpack)

## Summary
This lesson packages a small "portable power" demo which powers a Raspberry Pi Pico and shows status text on an LCD1602 (I2C). It includes a small UI and the `lcd1602.py` driver so the project can run standalone on a Pico.

## Files in this folder
- `main.py` — entry point; intended to run on power connect
- `lcd1602.py` — LCD1602 I2C driver (copied/adapted for this lesson)
- `IMG_7028.jpg` — reference photo of the prototype (converted from HEIC)

## Wiring (if testing on a breadboard)
- SDA -> GP6
- SCL -> GP7
- VCC -> 3V3 (or 5V if your backpack and LCD are known to tolerate it)
- GND -> GND

## How to use
1. Copy `main.py` and `lcd1602.py` to the Pico root (place `main.py` as the auto-run script).
2. Connect the LCD following the wiring above.
3. Power the Pico — `main.py` will run automatically and show status on the LCD.

If you want to debug interactively, remove/rename `main.py` and use the REPL or run the script from `mpremote`.

## Notes
- `lcd1602.py` in this folder is a minimal driver that expects the I2C backpack address `0x27` or `0x3F`.
- If you experience `OSError: [Errno 5] EIO` on writes, check wiring, VCC/GND, and try the `test.py` diagnostic in the LCD lesson for further troubleshooting.

---
Files and wiring follow the same conventions used throughout this repository. If you want me to trim the reference photo or include a schematic, tell me which format you prefer.
