# Raspberry Pi Pico Learning Labs (MicroPython)

This repository documents my step-by-step learning process with Raspberry Pi Pico and MicroPython.
Each folder is a single lesson focused on one topic: GPIO, LED patterns, ADC reading, PWM output, RGB control, arrays, and loops.

The project is designed as a practical learning portfolio:

- One folder = one lesson
- One `main.py` per lesson
- Clear expected behavior on real hardware

## Learning Path

| Lesson | Folder | Topic | Status |
| --- | --- | --- | --- |
| 00 | `00_TurnAllOff` | GPIO output basics and safe LED reset | Done |
| 01 | `01_FirstProject` | Built-in LED blink | Done |
| 02 | `02_FirstProgram` | Timed LED sequence (SOS-style practice) | Done |
| 03 | `03_ledsPattern` | Multi-LED animation patterns | Done |
| 04 | `04_binaryLeds` | Binary representation with LEDs | Done |
| 05 | `05_If` | Conditional logic with potentiometer thresholds | Done |
| 06 | `06_ReadingVoltages` | ADC reading and value conversion | Done |
| 09 | `09_PulseWithModulation` | PWM output from user input | Done |
| 10 | `10_DimmableLed` | LED dimming with PWM | Done |
| 11 | `11_ContollinRGBLed` | Interactive RGB color control | Done |
| 12 | `12_arrays&loops` | Arrays and loop practice in Python | Done |
| 13 | `13_arrays2` | Validated color list + RGB blink sequence | In progress |

## Hardware

Typical components used across lessons:

- Raspberry Pi Pico / Pico W
- Breadboard and jumper wires
- LEDs (single and RGB)
- Current-limiting resistors
- Potentiometer

## Software Setup

1. Install MicroPython firmware on the Pico.
2. Use VS Code with MicroPico extension (or Thonny as an alternative).
3. Open one lesson folder.
4. Upload and run `main.py` on the board.

## How To Use This Repository

1. Start from lesson `00` and continue in order.
2. Read each lesson README before running code.
3. Compare your observed hardware behavior against the expected behavior.

## Notes About Naming

Some folder names keep original learning-stage spelling for history consistency.
A future cleanup pass can rename folders and variable names while preserving lesson content.

## Credits

This learning path follows and adapts concepts inspired by Paul McWhorter tutorials.
This repository focuses on my own practice, implementation, and progress tracking.
