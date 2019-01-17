from login import login
from firebase_admin import auth

login()
users = list(auth.list_users().iterate_all())

print('Users: ' + str(len(users)))

