const { isUtf8 } = require("buffer");
const fs = require("fs");

// fs.writeFile("message.txt", "Hello from NodeJS!", (err) => {if (err) throw err;console.log("The file has been save!")});


fs.readFile("./message.txt","Utf8",(err,data) => {
    if (err) throw err;
    console.log(data);
});
