#!/usr/bin/node

// importing request mod
const request = require('request');

// gets the movie ID
const movieId = process.argv[2];

// building Star Wars api
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// creating GET request to Star Wars API
request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
    } else {
        const movieData = JSON.parse(body);

        console.log(movieData.title);
    }
});