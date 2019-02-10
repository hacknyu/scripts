from firebase_admin import firestore
from login import login

from datetime import datetime
import json

login()
db = firestore.client()

id_to_checkin = {}

for doc in db.collection('admitted').get():
    doc_dict = doc.to_dict()
    if 'checkinTimestamp' in doc_dict and doc_dict['checkinTimestamp'] != '':
        doc_dict['checkinTimestamp'] = datetime.fromtimestamp(doc_dict['checkinTimestamp'].timestamp())
    id_to_checkin[doc.id] = doc_dict

with open('checkin.json', 'w') as outfile:
    json.dump(id_to_checkin, outfile, ensure_ascii=False, default=str)
