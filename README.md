# coffee-addicts

Prerequisites:
    python >= 3.8
    pandas = 1.5.2
Run example:
    python main.py 3.3 2 https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv

Observation: 
    In the problem description below the coffee shop csv is described to be `Name,Y Coordinate,X Coordinate`,
    but then the given example (Input and expected_output) would not match. In order to match, the csv file 
    is actually `Name,X Coordinate,Y Coordinate`. The application was designed to work in order to match the given example, so the csv file should have this structure: `Name,X Coordinate,Y Coordinate`.

## Overview

You have been hired by a company that builds a app for coffee addicts.  You are 
responsible for taking the user’s location and returning a list of the three closest coffee shops.

## Input

The coffee shop list is a comma separated file with rows of the following form:
`Name,Y Coordinate,X Coordinate`

The quality of data in this list of coffee shops may vary.  Malformed entries should cause the 
program to exit appropriately. 

Your program will be executed directly from the command line and will be provided three 
arguments in the following order:
`<user x coordinate> <user y coordinate> <shop data url>`

Notice that the data file will be read from an network location (ex: https://raw.githubusercontent.com/Agilefreaks/test_oop/master/coffee_shops.csv)

## Output

Write a program that takes the user’s coordinates encoded as listed above and prints out a 
newline­separated list of the three closest coffee shops (including distance from the user) in 
order of closest to farthest.  These distances should be rounded to four decimal places. 

Assume all coordinates lie on a plane.

The output should be very simple no UI is required.

## Example

Using the [coffee_shops.csv](coffee_shops.csv)

__Input__

`47.6 -122.4 coffee_shops.csv`

__Expected output__

```
Starbucks Seattle2,0.0645
Starbucks Seattle,0.0861
Starbucks SF,10.0793
```

