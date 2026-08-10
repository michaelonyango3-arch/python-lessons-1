# Weekly Fitness Tracker

def calculate_average(numbers):
    """Returns the average of a  list of numbers"""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def hit_goal(steps, goal=8000):
    """Returns True?False if depending on whether steps met the goal"""
    return steps >= goal

def classify_day(steps, water, goal=8000, water_goal=8):
    """Returns a status string based on steps and water intake"""
    steps_ok = hit_goal(steps, goal)
    water_ok = water >= water_goal

    if steps_ok and water_ok:
        return "Great day"
    elif steps_ok or water_ok:
        return "Decent day"
    else: 
        return "Needs Improvement"
def day_report(day_name, steps, water, protocol="Standard"):
    """Prints a formatted report for a single day."""
    status= classify_day(steps, water)
    print(f"{day_name:<10} | Steps: {steps:<6} | Water {water:<3} | "
          f"Protocol: {protocol:<10} | {status}")

def weekly_summary(steps_list, water_list):
    """Returns average steps and average water for the week"""
    avg_steps= calculate_average(steps_list)
    avg_water= calculate_average(water_list)
    return avg_steps, avg_water

#-----------------------
# Data for the week
#----------------------

days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
steps_data = [9200, 7500, 11000, 8800, 6200, 10500, 9400]
water_data = [8, 6, 9, 7, 5, 8, 8]
protocols = ["OMAD", "2MAD", "OMAD", "Standard", "2MAD", "OMAD", "Standard", ]

#--------------------
# Run the reports
#--------------------

for i in range(len(days)):
    day_report (days[i], steps_data[i], water_data[i], protocols[i])

avg_steps, avg_water = weekly_summary(steps_data, water_data)

print("\n--- Weekly Summary ---")
print(f"Average Steps: {avg_steps:.1f}")
print(f"Average Water: {avg_water:.1f}")
print(f"Daily goal hit: {sum(hit_goal(s) for s in steps_data)} / {len(steps_data)}")


