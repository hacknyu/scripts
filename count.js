const fs = require('fs')

function main() {
  jsonData = fs.readFileSync('data.json')
  data = JSON.parse(jsonData)
  
  submitted = getSubmitted(data)
  console.log(`Total users: ${Object.keys(data).length}`)
  console.log(`Total submitted apps: ${submitted.length}`)
}

function getSubmitted(data) {
  let submitted = []
  
  for (let id in data) {
    if ('submitTimestamp' in data[id]) {
      submitted.push(data[id])
    }
  }

  return submitted
}

main()
