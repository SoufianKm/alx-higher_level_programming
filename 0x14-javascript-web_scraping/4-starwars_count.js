#!/usr/bin/node
// Script that prints the number of movies where
// the character “Wedge Antilles” is present.
//
//   The first argument is the API URL of the Star wars API: https://swapi-api.alx-tools.com/api/films/
//   Wedge Antilles is character ID 18 - your script must use this ID for filtering the result of the API
//   You must use the module request

const request = require('request');
let num = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const content = JSON.parse(body);
  content.results.forEach((film) => {
    film.characters.forEach((character) => {
      if (character.includes(18)) {
        num += 1;
      }
    });
  });
  console.log(num);
});
