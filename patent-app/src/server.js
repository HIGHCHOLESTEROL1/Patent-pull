const express = require('express');
const { spawn } = require('child_process');
const app = express();
const port = 3001; // Choose a port for your server

app.get('/run-python', (req, res) => {
    const pythonProcess = spawn('python', ['./controller/Control.py']);

    pythonProcess.stdout.on('data', (data) => {
        console.log(`stdout: ${data}`);
        res.write(data);
    });

    pythonProcess.stderr.on('data', (data) => {
        console.error(`stderr: ${data}`);
        res.write(data);
    });

    pythonProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        res.end(`child process exited with code ${code}`);
    });
});

app.get('/run-javaScript', (req, res) => {
    const javaScriptProcess = spawn('javaScript',['./dataReader.js']);
    
    javaScriptProcess.on('data', (data) => {
        console.log(`stdout: ${data}`);
        res.write(data);
    });

    javaScriptProcess.on('data', (data) => {
        console.error(`stderr: ${data}`);
        res.write(data);
    });

    javaScriptProcess.on('close', (code) => {
        console.log(`child process exited with code ${code}`);
        res.end(`child process exited with code ${code}`);
    });
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
