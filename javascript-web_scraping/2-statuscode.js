#!/usr/bin/node

// import request module
const request = require('request');

// getting url from cmdline
const url = process.argv[2];

// GET requestuest to url, prints status code is successful
request(url, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
