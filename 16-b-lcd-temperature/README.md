# Lesson 16B - LCD Temperature (I2C + DHT11)

## Status
Done, but with some stability issues to work on.

## Objective

Combine DHT11 readings with LCD1602 output so temperature and humidity are shown on screen, with unit toggle support (C/F) using a button.

## Files In This Lesson
- `main.py`: reads DHT11 values, handles button input, and writes data to LCD 
- `lcd1602.py`: I2C LCD1602 driver used by this lesson

## What Happened In Practice

This lesson worked in parts, but not always together:

- LCD driver can work correctly in standalone tests.
- DHT11 can print values in terminal when isolated.
- Integration in one loop became unstable during troubleshooting.

Main friction points found so far:

- DHT11 is sensitive to read timing.
- Very fast loops can trigger intermittent `measure()` failures.
- LCD behavior can look dead when writes only happen in conditional branches.

## Current Diagnostics

- Keep sensor output visible in terminal first.
- Use around 1 second between DHT11 reads for stable measurements.
- Show a startup LCD message to validate I2C/display independently.
- Once both parts are stable alone, re-enable combined display logic.

## Next Step

Stabilize `main.py` with this order:

1. Confirm LCD startup message appears.
2. Confirm DHT11 prints stable values in terminal.
3. Update LCD at a controlled interval using validated sensor data.
4. Re-test C/F toggle without breaking refresh flow.
