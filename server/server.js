const express = require('express')
const cors = require('cors')
const multer = require('multer')
const app = express()

const path = require('path')
const port = 3000

const upload = multer({ dest: path.join('public', 'media', 'images') })

app.use(express.static('public'))
app.use(cors())
app.use(express.json())
app.use(express.urlencoded({ extended: false }))

app.set('view engine', 'ejs')

app.post('/upload', upload.single('file'), (req, res) => {
  console.log(req.file)

  res.redirect('/')
})

app.get('/', (req, res) => {
  res.render('index')
})

app.use((req, res) => {
  res.status(404).send(req.url + ' NOT FOUND')
})

app.listen(port, () => {
  console.log(`Server now listening in port: ${port}`)
})
