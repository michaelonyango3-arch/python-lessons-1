#Dictionary 

daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5,
    "junk_entry": "delete me"
}




print("Steps today:", daily_log["steps"])
print("Water glasses:", daily_log["water_glasses"])
print("Cold shower:", daily_log["cold_shower"])
print("Fasting Protocal:", daily_log["fasting_protocol"])
print("Sleep hours:", daily_log["sleep_hours"])


# Add a new key

daily_log["pages_read"] = 30
print("After adding pages_read:", daily_log)


#Updating an existing key

daily_log["steps"] = 10400
print("After updating steps:", daily_log)

#Deleting a key

del daily_log["junk_entry"]
print(daily_log)

#Checking if a key exists

if "steps" in daily_log:
    print("Steps recorded:", daily_log["steps"])
if "sleep_hours" not in daily_log:
    print("Sleep hours not logged yet.")


# Trial

client = {
    "name": "James",
    "weight_kg": 84.5,
    "goal": "fat loss",
    "fasting_protocol": "2MAD",
    "bench_press_kg": 80,
    "weekly_session": 4
}
print("Client profile:")
for key, values in client.items():
    print(f" {key}:{values}")

print()

if client["bench_press_kg"] >= 80:
    print("Bench press goal hit.")


#my log

my_log = {
    "steps": 10000,
    "water_glasses": 12,
    "fasting_protocol": "OMAD",
    "cold_shower": True,
    "sleep_hours": 8,
}

print("My Log")

for key, value in my_log.items():
    print(f" {key}: {value}")

print()

if my_log["steps"] >= 10000:
    print("Steps goal hit.")







