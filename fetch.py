import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import json
from datetime import datetime
import inspect

cred = credentials.Certificate('certs.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://hacknyu-3e0c8.firebaseio.com'
})

db = firestore.client()
id_to_user = {}

for doc in db.collection('users').get():
    doc_dict = doc.to_dict()
    # a hack, but convert to native python datetime
    if 'submitTimestamp' in doc_dict:
        doc_dict['submitTimestamp'] = datetime.fromtimestamp(doc_dict['submitTimestamp'].timestamp())
    id_to_user[doc.id] = doc_dict

# we don't pickle b/c it's a security risk
with open('data.json', 'w') as outfile:
    json.dump(id_to_user, outfile, ensure_ascii=False, default=str)

print('Written to: data.json')
