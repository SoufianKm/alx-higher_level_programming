#!/usr/bin/node
// script that prints all characters of a Star Wars movie:
//
//   The first argument is the Movie ID - example: 3 = “Return of the Jedi”
//   Display one character name by line
//   You must use the Star wars API
//   You must use the module request

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const content = JSON.parse(body);
  const characters = content.characters;
  for (const character of characters) {
    request.get(character, (error, response, body) => {
      if (error) {
        console.log(error);
      } else {
        const names = JSON.parse(body);
        console.log(names.name);
      }
    });
  }
});
