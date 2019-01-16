import json
from datetime import timedelta, date
from dateutil import parser

with open('data.json', 'r') as read_file:
    data = json.load(read_file)

def filter_dict(func, dictionary):
    filtered = filter(lambda item: func(*item), dictionary.items())
    return { key: value for key, value in filtered }

def is_under_18(bday_str, event_date = date(2019, 2, 15)):
    earliest_bday = date(event_date.year - 18, event_date.month, event_date.day)
    try:
        bday = parser.parse(bday_str).date()
        return bday > earliest_bday
    except Exception as e:
        print(bday_str)
        print(e)
        return True

submitted = filter_dict(lambda uid, user: 'submitTimestamp' in user, data)
under_18 = filter_dict(lambda uid, user: is_under_18(user['birthDate']), submitted)

print('Total: ' + str(len(data)))
print('Submitted: ' + str(len(submitted)))
print('Under 18: ' + str(len(under_18)))
