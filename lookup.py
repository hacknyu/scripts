import json
from firebase_admin import auth
from login import login


login()
uid = input('UID? ').strip()

with open('data.json', 'r') as read_file:
    data = json.load(read_file)

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(str(key) + ': ' + str(value))

user = auth.get_user(uid)

print(user.display_name)
print(user.email)

print('Application:')
print('============')
print_dict(data[uid])
