# Daily discipline grader

steps = 7500
sleep_hours = 6
water_glasses = 5
cold_shower = False
pages_read = 5

if steps >= 10000:
    print ("Excellent job")
elif steps >= 7500:
    print ("Good job, but you can do better")
else:
    print ("You need to work more on your steps")

    if sleep_hours >= 7:
        print ("Good job on your sleep")
    else: 
        print ("You need to work more on your sleep")

if water_glasses >= 8:
    print ("Good job on your water intake")
else:
    print ("You need to take more water")

if cold_shower: 
    print ("Completed")
else:
    print("Skipped")

if pages_read >= 10:
    print ("Good job on your reading")
else: 
    print ("You need to read more")

    print(f"steps: {steps} sleep_hours: {sleep_hours} water_glasses: {water_glasses} cold_shower: {cold_shower} pages_read: {pages_read}")
    