#!/usr/bin/node

// impoting node file system mod
const fs = require('fs');

// get file path from cmdline
const filePath = process.argv[2];
// get string to write from second arg
const contentToWrite = process.argv[3];

// writes content to files asynchronously and handles errors and prints
fs.writeFile(filePath, contentToWrite, 'utf-8', (err) => {
    if (err) {
        console.error(err);
    }
});