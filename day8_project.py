#CONTACT BOOK

contacts = [
    {"name": "Michael Rolf", "phone": "0759300849", "skill": "Python Developer", "location": "Nairobi"},
    {"name": "James Ochiel", "phone": "0723456789", "skill": "Data Analyst", "location": "Kisumu"},
    {"name": "Sandra Wanjiku", "phone": "0712345678", "skill": "Web Developer", "location": "Nairobi"},
    {"name": "Patrick Ochieng", "phone": "0709876543", "skill": "Mobile App Developer", "location": "Nakuru"},
    {"name": "John Doe", "phone": "0711111111", "skill": "UI/UX Designer", "location": "Nairobi"},
]

print("Contacts stored:", len(contacts))
print(contacts[0])

print("====CONTACT BOOK====")
for i, contact in enumerate(contacts):
    print(f"\n{i+1}. {contact['name']}")
    print(f"  Phone: {contact['phone']}")
    print(f"  Skill: {contact['skill']}")
    print(f"  Location: {contact['location']}")

search_name = "James Ochiel"
found_contact = False

for contact in contacts:
    if contact["name"] == search_name:
        print("Contact found:")
        print(f" Name: {contact['name']}")
        print(f" Phone: {contact['phone']}")
        print(f" Skill: {contact['skill']}")
        print(f" Location: {contact['location']}")
        found_contact = True
        break

if not found_contact:
    print(f"Contact '{search_name}' not found.")


search_city = "Nairobi"
print(f" Contacts in {search_city}:")

for contact in contacts:
    if contact["location"] == search_city:
        print(f" - {contact['name']} ({contact['skill']})")

print("Before:", len(contacts), "contacts")

#Add a new contact

new_contact = {
    "name": "Alice Mwangi",
    "phone": "0722222222",
    "skill": "Data Scientist",
    "location": "Nairobi"
}
contacts.append(new_contact)
print("After:", len(contacts), "contacts")
print("Last contact:", contacts[-1])


