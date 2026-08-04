# Loops

# SMP Prject

daily_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100]

minimum = 8000

for day in range(1, 8):
    print("Day", day, ":", daily_steps[day-1], "steps")

day = 1
while day <= 7:
    steps = daily_steps[day-1]
    current_day = day
    day += 1  # increment FIRST, so continue can never skip it

    if steps >= minimum:
        continue  # goal met, skip the "did not reach" message

    print("You did not reach your goal of", minimum, "steps on day", current_day)

# Ask the user for a number and print its multiplication table
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

 

