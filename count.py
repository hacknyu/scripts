import json
from datetime import timedelta, date
from dateutil import parser


with open('data.json', 'r') as read_file:
    data = json.load(read_file)

def filter_dict(func, dictionary):
    filtered = filter(lambda item: func(*item), dictionary.items())
    return { key: value for key, value in filtered }

def is_under_18(uid, form, event_date = date(2019, 2, 15)):
    bday_str = form['birthDate']
    earliest_bday = date(event_date.year - 18, event_date.month, event_date.day)
    try:
        bday = parser.parse(bday_str).date()
        return bday > earliest_bday
    except Exception as e:
        print('> ' + str(e))
        print('  ' + str(bday_str))
        print('  uid: ' + str(uid))
        return True

submitted = filter_dict(lambda uid, form: 'submitTimestamp' in form, data)

nyu = filter_dict(lambda uid, form: 'nyuSchool' in form, submitted)
shanghai = filter_dict(lambda uid, form: form['nyuSchool'] == 'shanghai', nyu)
abu_dhabi = filter_dict(lambda uid, form: form['nyuSchool'] == 'abu-dhabi', nyu)

postgrad = filter_dict(lambda uid, form: form['yearOfStudy'] == 'post-grad', submitted)
under_18 = filter_dict(lambda uid, form: is_under_18(uid, form), submitted)


print('Total: ' + str(len(data)))
print('Submitted: ' + str(len(submitted)))
print('NYU: ' + str(len(nyu)))
print('  Abu Dhabi: ' + str(len(abu_dhabi)))
print('  Shanghai: ' + str(len(shanghai)))
print('Postgrad: ' + str(len(postgrad)))
print('Under 18: ' + str(len(under_18)))
