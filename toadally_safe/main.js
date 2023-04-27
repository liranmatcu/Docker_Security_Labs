//npm install -g nodemon  //provides automatic restarts after edits so you don't have to restart manually
//npm install zxcvbn
//npm install --save express
//npm install body-parser

// nodemon main.js
// ^^^^^^^^^^^^^^^^ to start

const path = require('path');
const zxcvbn = require('zxcvbn');
const express = require('express'); //helps build web apps faster + more easily than Node.js alone
const bodyParser = require('body-parser'); //extracts body

var app = express();


app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(express.static(__dirname+'/public'));
//

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname+'/index.html'));

    
});

app.post('/password', (req, res) => {
    const password = req.body.password; //grab password from html password field
    const result = zxcvbn(password); //pass typed in password to zxcvbn
    res.json(result);   //give result

});




// work in progress



app.listen(3000);
// http://localhost:3000