from count import *
from count_users import users

import pickle

unused_users = []

for user in users:
    if user.uid not in data:
        unused_users.append(user)

pickle.dump(users, open('users.pickle', 'wb'))
pickle.dump(unused_users, open('unused.pickle', 'wb'))
