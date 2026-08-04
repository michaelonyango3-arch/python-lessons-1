#Week2 Assignment

#Create a list of five fruits

fruits = ["mango", "banana", "apple", "orange", "grape"]

#sort the list in alphabetical order and print it 

fruits.sort()
print("Sorted fruits:", fruits)

fruits.reverse()
print("Reversed fruits:", fruits)

fruits.append("Pawpaw")
print("After adding Pawpaw:", fruits)


#Exercise 2: Create a dictionary for a student with name, age, and grade.
#Print each value using a key

student = {
    "name": "Eric",
    "age": 25,
    "grade": "A"
}

for key, value in student.items():
    print(f"{key}: {value}")


#Exercise 3: Create a list of dictionaries for three students, each with name, age, and grade.
#Loop through and print each student's name and grade.

students = [
    {"name": "Eric", "age": 25, "grade": "A"},
    {"name": "Jane", "age": 22, "grade": "B"},
    {"name": "John", "age": 24, "grade": "A"}
]
for s in students:
    print(f"Name: {s['name']}, Grade: {s['grade']}")


#Exercise 4: Challenge
#Store 3 contacts as a dictionary with name: number
#Print a formattted contact list

contacts = {
    "Dad": "0715329060",
    "Mum": "0793711576",
    "Wife": "0746755063"
}

print('---Contact List---')
for name, number in contacts.items():
    print(f"{name}: {number}")
    


