[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/z8haBqsC)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15359969&assignment_repo_type=AssignmentRepo)
# epai5session5-template
EPAi5 Session 5 Template


## Overview

This repository contains several utility functions that perform various calculations and conversions. The functions included are:

1. `time_it`
2. `squared_power_list`
3. `polygon_area`
4. `temp_converter`
5. `speed_converter`

Each function is designed to perform a specific task, ranging from timing the execution of other functions to converting temperatures and calculating the area of polygons. Below is a detailed explanation of each function.

## Function Descriptions

### 1. `time_it`

**Purpose:**  
The `time_it` function measures the average time taken to execute a specified function a given number of times.

**Parameters:**  
- `fn`: The function to be timed.
- `*args`: Positional arguments to pass to the function `fn`.
- `repetitions`: The number of times to execute the function `fn` (default is 1).
- `**kwargs`: Keyword arguments to pass to the function `fn`.

**Returns:**  
The average time taken to execute the function `fn` over the specified number of repetitions.

**Usage Example:**
```python
def fn(x):
	return x * x

average_time = time_it(fn, *args, repetitions= 1, **kwargs)
print(average_time)
```

### 2. `squared_power_list`

**Purpose:**  
The `squared_power_list` function generates a list of powers of a given number, ranging from a specified start power to an end power.

**Parameters:**  
- `number`: The base number (must be an integer less than or equal to 10).
- `start`: The starting power (default is 0).
- `end`: The ending power (default is 5).
- `*args`: Positional arguments (none expected).
- `**kwargs`: Keyword arguments (none expected).

**Returns:**  
A list of powers of the `number`, starting from `number**start` to `number**(end-1)`.

**Usage Example:**
```python
powers_list = squared_power_list(2, start=1, end=4)
print(powers_list)  # Output: [2, 4, 8]
```

### 3. `polygon_area`

**Purpose:**  
The `polygon_area` function calculates the area of a regular polygon with a specified number of sides and side length.

**Parameters:**  
- `length`: The length of each side of the polygon (must be a positive integer).
- `sides`: The number of sides of the polygon (default is 3, must be between 3 and 6).
- `*args`: Positional arguments (none expected).
- `**kwargs`: Keyword arguments (none expected).

**Returns:**  
The area of the polygon.

**Usage Example:**
```python
area = polygon_area(5, sides=4)
print(area)  # Output: 25
```

### 4. `temp_converter`

**Purpose:**  
The `temp_converter` function converts a temperature from Celsius to Fahrenheit or vice versa.

**Parameters:**  
- `temp`: The temperature to convert (must be an integer or float).
- `temp_given_in`: The unit of the input temperature, either 'c' for Celsius or 'f' for Fahrenheit (default is 'f').
- `*args`: Positional arguments (none expected).
- `**kwargs`: Keyword arguments (none expected).

**Returns:**  
The converted temperature.

**Usage Example:**
```python
converted_temp = temp_converter(100, temp_given_in='c')
print(converted_temp)  # Output: 212.0
```

### 5. `speed_converter`

**Purpose:**  
The `speed_converter` function converts speed from kilometers per hour (km/h) to various other units.

**Parameters:**  
- `speed`: The speed in km/h (must be a positive integer or float, less than or equal to the speed of light).
- `dist`: The distance unit to convert to (default is 'km', options are 'km', 'm', 'ft', 'yrd').
- `time`: The time unit to convert to (default is 'min', options are 'ms', 's', 'min', 'hr', 'day').
- `*args`: Positional arguments (none expected).
- `**kwargs`: Keyword arguments (none expected).

**Returns:**  
The converted speed.

**Usage Example:**
```python
converted_speed = speed_converter(60, dist='m', time='s')
print(converted_speed)  # Output: 16
```

## Error Handling

Each function includes extensive error handling to ensure proper usage. Common errors that are checked include:
- Invalid types for parameters.
- Out-of-range values for parameters.
- Excess positional or keyword arguments.

These validations help maintain the integrity of the functions and provide meaningful error messages to guide correct usage.

## Conclusion

This repository provides a collection of utility functions that can be used for various mathematical and conversion tasks. Each function is designed with robustness and ease of use in mind, making them valuable tools for a wide range of applications.







