import json

uid = input('UID? ').strip()

with open('data.json', 'r') as read_file:
    data = json.load(read_file)

def print_dict(dictionary):
    for key, value in dictionary.items():
        print(str(key) + ': ' + str(value))

print_dict(data[uid])
