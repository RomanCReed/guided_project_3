const express = require("express");
const app = express();
const PORT = 4000;

app.get('/', (req, res) => {
    console.log('in model GET request');
    const {spawn} = requre('child_process');
    const model = spawn('python', ['../trained_model.pkl']);
})




app.listen(PORT, () => {
    console.log(`Server is running http://localhost:${PORT}`);
});