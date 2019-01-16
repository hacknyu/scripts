const admin = require('firebase-admin')
const fs = require('fs')

const serviceAccount = require('./certs.json')
const settings = {
  timestampsInSnapshots: true 
}

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: 'https://hacknyu-3e0c8.firebaseio.com'
})

const db = admin.firestore()
db.settings(settings)

async function getData() {
  const snapshot = await db.collection('users').get()
  const data = {}
  snapshot.forEach(doc => data[doc.id] = doc.data())
  fs.writeFileSync('data.json', JSON.stringify(data))     
}

getData()
