#Nested Data and String methods

weekly_log = [

    {"day": "Monday", "steps": 9200, "protocol": "OMAD", "cold_shower": True
    },
    {"day": "Tuesday", "steps": 10500, "protocol": "2MAD", "cold_shower": True
    },
    {"day": "Wednesday", "steps": 8800, "protocol": "OMAD", "cold_shower": False
    },
    {"day": "Thursday", "steps": 11000, "protocol": "Autography Marathon", "cold_shower": True
     },
     {"day": "Friday", "steps": 7600, "protocol": "OMAD", "cold_shower": True
      }

]

print(weekly_log)

#first day step count

print("Monday steps:", weekly_log[0]["steps"])

#third day's protocol

print("Wednesday protocol:", weekly_log[2]["protocol"])

#second day, all details

print("Tuesday details:", weekly_log[1])


for log in weekly_log:
    status = "Goal hit" if log["steps"] >= 8000 else "Goal not hit"
    print(log["day"], "-", log["steps"], "steps -", status)

for log in weekly_log:
    status = "Cold shower taken" if log["cold_shower"] else "No cold shower"
    print(log["day"], "-", status)

weekly_summary = {
    "week": 1,
    "steps": [9200, 10500, 8800, 11000, 7600],
    "protocol": ["OMAD", "2MAD", "OMAD", "Autography Marathon", "OMAD"],
    "cold_shower completed": 4,
}

print("Week:", weekly_summary["week"])
print("Total days tracked:", len(weekly_summary["steps"]))
print("First day steps:", weekly_summary["steps"][0])
print("Average steps:", sum(weekly_summary["steps"]) / len(weekly_summary["steps"]))


clients = [
    {"name": "James", "goal": "fat loss", "weekly_sessions": 4, "bench_press_kg": 80},
    {"name": "Mwangi", "goal": "muscle gain", "weekly_sessions": 5, "bench_press_kg": 100},
    {"name": "Sandra", "goal": "endurance", "weekly_sessions": 3, "bench_press_kg": 50},
    {"name": "Patrick", "goal": "fat loss", "weekly_sessions": 4, "bench_press_kg": 70}
]

print("Fat loss clients:")
for client in clients:
    if client["goal"] == "fat loss":
        print("-", client["name"], "| Bench:", client["bench_press_kg"], "kg | Sessions:", client["weekly_sessions"])


#exercise

weekly_log = [
    {"day": "Monday", "steps": 10000, "protocol": "OMAD"},
    {"day": "Tuesday", "steps": 12000, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8000, "protocol": "2MAD"},
    {"day": "Thursday", "steps": 9000, "protocol": "Autography Marathon"},
    {"day": "Friday", "steps": 7000, "protocol": "OMAD"},
]

total = 0
for log in weekly_log:
    print(log["day"], "|", log["steps"], "steps |", log["protocol"])
    total += log["steps"]

average = total / len(weekly_log)
print()
print("Average steps:", average)

for log in weekly_log:
    status = "Autography Marathon completed" if log["protocol"] == "OMAD" else "Autography Marathon not completed"
    print(log["day"], "-", status)


