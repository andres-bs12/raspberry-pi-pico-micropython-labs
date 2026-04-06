# Lesson 14 - Push Buttons and Pull-Up Resistors

<details>
<summary>Reference video</summary>

[Paul McWhorter - Lesson 17](https://www.youtube.com/watch?v=OkaUMOH6CSI&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=17)

</details>

## Objective

Learn how a push button works with a pull-up resistor and use it to control an LED.
The button acts like a toggle: each press changes the LED state and keeps it that way until the next press.


## Code

- `main.py`

## Expected Behavior

1. When the button is not pressed, the input reads `1`.
2. When the button is pressed, the input reads `0`.
3. Pressing the button once turns the LED on.
4. Pressing it again turns the LED off.
5. The LED stays in its last state until the next press.

## What You Practice

- Reading digital inputs from a push button
- Using `Pin.IN` with `Pin.PULL_UP`
- Detecting a button press edge
- Toggling an output state
- Basic debouncing

## Note

With a pull-up resistor, the button input is normally high (`1`) and goes low (`0`) when pressed.
That means the code should detect the transition from `1` to `0`, not just the current button value.