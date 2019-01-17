import pickle

users = pickle.load(open('users.pickle', 'rb'))
unused = pickle.load(open('unused.pickle', 'rb'))

def print_user(user):
    print(user.email)
    if user.display_name:
        print(user.display_name)
    if len(user.provider_data) > 1:
        for user_info in user.provider_data:
            print('  ' + str(user_info))
    print(user.provider_id)
    print('---------------')

nyu_email = []
for user in unused[:]:
    print_user(user)
    if 'nyu.edu' in user.email:
        nyu_email.append(user.email)

print(len(unused))
print(len(nyu_email))
print(nyu_email)
