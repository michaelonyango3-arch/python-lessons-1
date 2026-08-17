# List Comprehensions and Lambda

# List Comprehension

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Transforming items
# Convert each step count into km

km_walked = [round(s * 1.3 / 1000, 2) for s in weekly_steps]
print("Steps:", weekly_steps)
print("km  :", km_walked)

# Convert each step into calories burned (0.04 cal / step)

calories_burned = [round(s * 0.04, 2) for s in weekly_steps]
print("Steps:", weekly_steps)
print("Calories:", calories_burned)


clients = [
    {"name": "James", "goal": "fat loss", "sessions": 4},
    {"name": "Mwangi", "goal": "muscle gain", "sessions": 5},
    {"name": "Sandra", "goal": "endurance", "sessions": 3},
    {"name": "Patrick", "goal": "fat loss", "sessions": 4}
]

# Get the names of all fat loss clients
fat_loss_names = [c["name"] for c in clients if c["goal"] == "fat loss"]
print("Fat_loss_clients:", fat_loss_names)

# Get all clients with 4 or more sessions per week
active_clients = [c["name"] for c in clients if c["sessions"] >= 4]
print("Active clients:", active_clients)

workouts = [
    {"exercise": "squat", "weight_kg": 80, "reps": 8},
    {"exercise": "bench", "weight_kg": 60, "reps": 10},
    {"exercise": "deadlift", "weight_kg": 100, "reps": 5},
    {"exercise": "row", "weight_kg": 50, "reps": 12},
]

# Comprehension: Build a list of total volune(weight * reps ) per exercise

volume = [w["weight_kg"] * w["reps"] for w in workouts]
print("Volumes:", volume)

# Comprehension: filter exercise with volume over 500

heavy_lifts = [w["exercise"] for w in workouts if w["weight_kg"] * w["reps"] > 500]
print("Heavy lifts:", heavy_lifts)

for w in workouts:
    volume = w["weight_kg"] * w["reps"]
    if volume > 550:
        intensity = "heavy"
    elif volume > 400:
        intensity = "moderate"
    else:
        intensity = "light"
    w["volume"] = volume #mutating the dict
    w["intensity"] = intensity #mutating the dict
    print(f"{w['exercise']:>9} : {volume} volume -> {intensity}")


weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Build a list of status strings for each day
statuses = ["Goal hit" if s >= 8000 else "Below goal" for s in weekly_steps]

for i, status in enumerate(statuses):
    print(f"Day {i+1}: {weekly_steps[i]} steps - {status}")


# Exercise

people = [
    {"name": "James", "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200]},
    {"name": "Sandra", "steps": [7000, 7500, 6800, 8000, 7200, 8500, 7800]},
    {"name": "Mwangi", "steps": [10000, 11500, 9800, 12000, 10500, 11000, 10800]},
    {"name": "Patrick", "steps": [8500, 9000, 8800, 9200, 8600, 9400, 9100]},
]

# 1. All step counts above 10,000 across all peopl
all_steps = [s for p in people for s in p["steps"]]
high_steps = [s for s in all_steps if s >= 10000]
print("steps above 10000:", high_steps)

# 2. Names with average steps above 9000
high_avg_names = [p["name"] for p in people if sum(p["steps"]) / len(p["steps"]) > 9000]
print("High average perfomers:", high_avg_names)

