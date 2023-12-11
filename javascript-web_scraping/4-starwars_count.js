#!/usr/bin/node

// importing request mod
const request = require('request');

// gets the API URL from args
const apiUrl = process.argv[2];

// character id for 'wedge antilles'
const characterId = 18;

// creating GET request to Star Wars API file endpoint
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    // parse JSON response
    const filmsData = JSON.parse(body);

    // Filter films w/ "Wedge Antilles" is
    const withWedge = filmsData.results.filter((film) =>
      film.characters.includes(`https://swapi-api.hbtn.io/api/people/${characterId}/`)
    );

    console.log(withWedge.length);
  }
});
