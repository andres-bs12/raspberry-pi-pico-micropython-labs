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
| 00 | `00_turn-all-off` | GPIO output basics and safe LED reset | Done |
| 01 | `01_first-project` | Built-in LED blink | Done |
| 02 | `02_first-program` | Timed LED sequence (SOS-style practice) | Done |
| 03 | `03_leds-pattern` | Multi-LED animation patterns | Done |
| 04 | `04_binary-leds` | Binary representation with LEDs | Done |
| 05 | `05_if` | Conditional logic with potentiometer thresholds | Done |
| 06 | `06_reading-voltages` | ADC reading and value conversion | Done |
| 09 | `09_pulse-with-modulation` | PWM output from user input | Done |
| 10 | `10_dimmable-led` | LED dimming with PWM | Done |
| 11 | `11_controlling-rgb-led` | Interactive RGB color control | Done |
| 12 | `12_arrays-and-loops` | Arrays and loop practice in Python | Done |
| 13 | `13_arrays-2` | Validated color list + RGB blink sequence | Done |
| 14 | `14_push-buttons` | Push button input basics | Done |

## Hardware

Typical components used across lessons:

- Raspberry Pi Pico / Pico W
- Breadboard and jumper wires
- LEDs (single and RGB)
- Current-limiting resistors
- Potentiometer
- yada yada yada... Or just get the Raspberry Pi Pico Starter Kitfor all-in-one convenience.

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

Lesson folders now follow one consistent standard:
`NN_topic-name` using lowercase letters and hyphens.

## Credits

This learning path follows and adapts concepts inspired by Paul McWhorter tutorials.
This repository focuses on my own practice, implementation, and progress tracking.
