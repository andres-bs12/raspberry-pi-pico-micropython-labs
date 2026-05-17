# Lesson 15 - Temperature and Humidity Sensor (DHT11)

<details>
<summary>Reference video</summary>

[Paul McWhorter - Lesson 17](https://www.youtube.com/watch?v=KYEidJFYPto&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=20)

</details>

## Objective

Read temperature and humidity from a DHT11 sensor using Raspberry Pi Pico and MicroPython.

## Code

- `main.py`

The script:

1. Initializes DHT11 on GPIO16.
2. Calls `measure()` inside `try/except` to avoid crashes from timeout errors.
3. Prints temperature and humidity continuously in the terminal.

## What Happened In Practice

This lesson did not work for me just by following the tutorial steps.

- I had to search for another explanation and found the answer here:
	[https://www.youtube.com/watch?v=_Z3U62duXbI](https://www.youtube.com/watch?v=_Z3U62duXbI)
- After that, I was able to get readings.
- Humidity does react to different situations (so that part seems to work).
- Temperature looks unreliable in my tests.

## Current Sensor Behavior

The temperature value stays around 26 to 27 C both inside and outside / no that cool.

Even testing outside (around 18 C), the sensor still reports almost the same value.
Because of that, I am not fully confident in the temperature accuracy right now.

## Honest Note

Sadly, I wanted to use this sensor in other projects, but with this behavior I still need to verify if the issue is wiring, calibration limits, sensor quality, the specific DHT11 unit, or me not understanding something about how it works (most likely).