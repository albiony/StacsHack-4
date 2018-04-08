const http = require('http');
var express = require('express');
var child_process = require("child_process");
//child_process.spawn = 
var spawn = require('cross-spawn');;
var app = express();
const port = 3000;

app.listen(3000);
app.use(express.static('Client'));
//app.get('/', serveStatic);
app.get('/calc/:origin-:dest-:passengers', runCalculation);

function serveStatic(req, res) {
    res.sendFile("./Client/index.html", { root: '.' });
    res.sendFile("./Client/client.js", { root: '.' });
}

function runCalculation(req, res) {
    var origin = req.params['origin'];
    var dest = req.params['dest'];
    var passengers = req.params['passengers'];

    var pythonProcess = spawn('python', ["./main.py", origin, dest, passengers]);
    pythonProcess.stdout.on('data', function (data) {
        res.send(data);
    });
}
