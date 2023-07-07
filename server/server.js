const express = require('express')
const cors = require('cors')
const app = express()

const port = 3000

app.use(cors())
app.use(express.json())
app.use(express.urlencoded({extended: false}))

app.set('view engine', 'ejs')

app.post('/upload', (req,res) => {})

app.get('/', (req, res) => {
  res.render('index')
})

app.use((req, res) => {
  res.status(404).send(req.url + ' NOT FOUND')
})

app.listen(port, () => {
  console.log(`Servr now listening in port: ${port}`)
})
