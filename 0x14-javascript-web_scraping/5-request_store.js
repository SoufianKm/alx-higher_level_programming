#!/usr/bin/node
// Script that gets the contents of a webpage and stores it in a file.
//
//   The first argument is the URL to request
//   The second argument the file path to store the body response
//   The file must be UTF-8 encoded
//   You must use the module request

const request = require('request');
const fs = require('fs');

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  fs.writeFile(process.argv[3], body, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
