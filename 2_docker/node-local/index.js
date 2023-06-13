const express = require('express');
const app = express();
const port = 3000;

app.use(function(req, res, next) {
    res.send('<h1>Olá Mundo!!!</h1>')
});

app.listen(port, function() {
    console.log('listening on port ' + port)
});