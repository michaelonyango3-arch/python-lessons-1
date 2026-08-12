# MODULES AND IMPORTING

#Maths module

import math

# Square root

print("Square root of 144:", math.sqrt(144))

# Round down and up

print("Floor of 7.9:", math.floor(7.9))
print("Ceiling of 7.1:", math.ceil(7.1))

# Pi

print("Pi:", math.pi)

# Power: 2 to the powe of 10
print("2 to the 10th:", math.pow(2,10))

import math

total_days = 50
training_days_per_week = 5
weeks = total_days / 7

print(f"Total days: {total_days}")
print(f"Full weeks: {math.floor(weeks)}")

# Distance calculation using Pythagoras 
walk_east = 3.0    # km
walk_north = 4.0   # km
distance = math.sqrt(walk_east **2 + walk_north**2)
print(f"Direct distance: {distance} km")


# Random module

import random

# Random integer between 1 and 10 (inclusive)

print("Random number:", random.randint(1, 10))

# Random float between 0 and 1
print("Random float:", random.random())

# Random choice from a list 
skills = ["welding", "tiling", "upholstery", "phone repair", "copywriting"]
print("Today's skill focus:", random.choice(skills))

# Shuffle a list
random.shuffle(skills)
print("Shuffled:", skills)

import random

print("Simulated step counts for this week:")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

for day in days:
    steps = random.randint(5000, 13000)
    status = "OK" if steps >= 8000 else "low"
    print(f" {day}: {steps} steps ({status})")


# Datetime module

from datetime import datetime, date

# Today's date and time

now = datetime.now()
print("Current datetime:", now)

# Just the date 

today = date.today()
print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# Days between two dates

start = date(2025, 1, 1)
end = date(2025, 12, 31)
delta = end - start
print("Days in 2025:", delta.days)


from datetime import date

# How many days until a goal date

today = date.today()
goal_date = date(2025, 12, 31)
days_left = (goal_date - today).days

print(f"Days until end of 2025: {days_left}")

# Format the date as text

formatted = today.strftime("%d %B %Y")
print("Today's date:", formatted)

# Importing specificic Functions

from math import sqrt, floor, ceil
from random import randint, choice

# No need to write mathsqrt() or random.randint()

print("Square root of 225:", sqrt(225))
print("Floor of 9.7:", floor(9.7))

protocols = ["OMAD", "2MAD", "Autography Marathon"]
print("Today's protocol:", choice(protocols))
print("Random step bonus:", randint(100, 500), "steps")


import random
import math


def generate_week():
    days = [ "Mon", "Tue", "Wed", "Thu", "Fri", "sat", "Sun"]
    total = 0
    goal_days = 0

    for day in days:
     steps = random.randint(6000, 12000)
     total += steps
     if steps >= 8000:
        goal_days += 1
     print(f" {day}: {steps} steps")

    avg = math.floor(total/7)
    print(f"\nAverage steps : {avg}")
    print(f"Days on goal : {goal_days}/7")

generate_week()











