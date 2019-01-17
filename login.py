import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def login():
    cred = credentials.Certificate('certs.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://hacknyu-3e0c8.firebaseio.com'
    })

