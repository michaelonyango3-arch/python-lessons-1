weekly_steps = [9200, 7400, 10500, 8800, 6900, 11000, 9600]

for steps in weekly_steps:
    if steps >= 8000:
        print(steps, "- Goal hit")
    else:
        print(steps, "- Below target")
print("Days tracked:", len(weekly_steps) )


skills = ["welding", "tiling", "upholstery"]
print("Before:", skills)

skills.append("phone repair")
print("After:", skills)

skills.append("graphic design")
print("Final:", skills)

skills.insert(1, "copywriting")
print("After:", skills)


habits = ["8 glasses of water", "cold shower", "OMAD fast", "workout", "cold shower"]
print("Before:", habits)

position = habits.index("cold shower")
print("Cold shower is at position:", position)

habits.remove("cold shower")
print("After:", habits)



weekly_steps = [9200, 10500, 8800,11000, 7600]
print("Before:", weekly_steps)


removed = weekly_steps.pop()
print("Removed:", removed)
print("After:", weekly_steps)

removed2 = weekly_steps.pop(1)
print("Removed:", removed2)
print("After:", weekly_steps)


weekly_steps = [9200, 10500, 8800, 11000, 7600]
print("Unsorted:", weekly_steps)

weekly_steps.sort()
print("Sorted low to high:", weekly_steps)

weekly_steps.sort(reverse=True)
print("Sorted high to low:", weekly_steps)

skills = ["welding", "tiliing", "upholstery", "phone repair", "graphic design", "copywriting"]
skills.reverse()
print(skills)

daily_results = ["hit", "miss", "hit", "hit", "miss", "hit", "miss"]
hit_count = daily_results.count("hit")
miss_count = daily_results.count("miss")
print("Days goal hit:", hit_count)
print("Days goal missed:", miss_count)


steps = [8800, 6500, 11000, 9200, 7300, 10500, 8000]

steps.append(9500)
steps.remove(6500)
steps.insert(3, 10000)

steps.sort(reverse=True)

print("Final list:", steps)

#count days over 9000
high_days = 0
for s in steps:
    if s >= 9000:
        high_days += 1
print("Days over 9000:", high_days)





