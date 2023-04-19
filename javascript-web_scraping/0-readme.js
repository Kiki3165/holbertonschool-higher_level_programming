#!/usr/bin/node

const fs = require("fs")

fs.readFile("0-readme.js", "utf8", (err, data) => {
    if (err) throw err;
    console.log(data.toString());
})