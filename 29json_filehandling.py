import json

user_data = {
    'users': [
        {'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
        {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'},
        {'id': 3, 'name': 'Charlie', 'email': 'charlie@example.com'}
    ],
    'last_updated': '2026-01-06'
}

with open("users.json","w") as file:
    json.dump(user_data, file, indent=4)

print("Data is saved to users.json")

with open("users.json","r") as file:
    file_data = json.load(file)

print(f"Number of users : ",len(user_data['users']))

for i in user_data['users']:
    print(f"id: {i['id']}, name: {i['name']}, email: {i['email']}")

