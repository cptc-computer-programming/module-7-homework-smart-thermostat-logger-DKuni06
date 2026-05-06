# Smart Thermostat Logger

## Overview

In this assignment, you will write a Python program that summarizes temperature readings from a smart thermostat sensor.

A smart thermostat records temperature readings from a room. Your program will ask the user how many readings they want to enter, collect each reading, validate the input, and then display a summary.

This assignment practices:

- `for` loops
- input validation with `while` loops
- running totals
- averages
- `if`, `elif`, and `else` logic

## Program Requirements

Write a Python program that does the following:

1. Ask the user how many temperature readings they want to enter.
2. Validate that the number of readings entered is greater than `0`.
3. Use a `for` loop to ask for each temperature reading.
4. Validate that each temperature is between `40` and `100` degrees, inclusive.
5. Keep a running total of all valid temperature readings.
6. Count how many readings are below the comfort range.
7. Count how many readings are above the comfort range.
8. Calculate the average temperature.
9. Display a summary.

## Comfort Range

For this assignment, use the following comfort range:

- Below `68` degrees: too cold
- From `68` through `76` degrees: comfortable
- Above `76` degrees: too warm

## Input Validation Rules

Your program must reject invalid input.

The number of readings must be greater than `0`.

Example invalid values:
```
0  
-3
```
Each temperature reading must be between `40` and `100`, inclusive.

Example invalid values:
```
25  
105  
-10
```
When invalid input is entered, display an error message and ask the user to enter the value again.

## Required Output

Your program must display:

- average temperature
- number of readings below the comfort range
- number of readings above the comfort range

The average temperature should be displayed with one digit after the decimal point.

## Sample Run
```
    Enter the number of temperature readings: 5
    Enter temperature reading 1: 67
    Enter temperature reading 2: 70
    Enter temperature reading 3: 72
    Enter temperature reading 4: 78
    Enter temperature reading 5: 74

    Smart Thermostat Summary
    ------------------------
    Average temperature: 72.2
    Readings below comfort range: 1
    Readings above comfort range: 1
```
## Sample Run with Input Validation
```
    Enter the number of temperature readings: 0
    Error: The number of readings must be greater than 0.
    Enter the number of temperature readings: 3
    Enter temperature reading 1: 25
    Error: Temperature must be between 40 and 100 degrees.
    Enter temperature reading 1: 65
    Enter temperature reading 2: 72
    Enter temperature reading 3: 101
    Error: Temperature must be between 40 and 100 degrees.
    Enter temperature reading 3: 80

    Smart Thermostat Summary
    ------------------------
    Average temperature: 72.3
    Readings below comfort range: 1
    Readings above comfort range: 1
```
## Submission

Submit a link to your automatically generated Feedback PR to the Canvas assignment.

## Tips

Use a running total variable to add up the temperature readings.

Example:
``` python
    total_temp += temp
```
Use a counter variable to count readings that are too cold or too warm.

Example:
``` python
    too_cold_count += 1
```
Use `format` to display the average with one decimal place.

Example:
``` python
    format(average_temp, ".1f")
```