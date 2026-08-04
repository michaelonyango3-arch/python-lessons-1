#TRAINERS PROGRAM

number_of_exercises = 6
sets_per_exercise = 4
reps_per_set = 10
average_weight_per_rep = 60 # in kilograms
session_duration_in_minutes = 45

total_sets = number_of_exercises * sets_per_exercise
total_reps = total_sets * reps_per_set
total_volume = total_reps * average_weight_per_rep
reps_per_minute = total_reps / session_duration_in_minutes
exceeded_10000_kilograms = total_volume > 10000

print(f"total sets: {total_sets}")
print(f"total reps: {total_reps}")
print(f"total volume lifted: {total_volume} kilograms")
print(f"reps per minute: {total_reps / session_duration_in_minutes}")
print(f"exceeded 10000 kilograms: {exceeded_10000_kilograms}")

