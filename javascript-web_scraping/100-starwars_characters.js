#!/usr/bin/node

const request = require('request');
const movie = process.argv[2];
const urlPath = 'https://swapi-api.hbtn.io/api/films/' + movie;

request(urlPath, (err, res, body) => {
  if (err) throw (err);
  const jsonBody = JSON.parse(body);

  jsonBody.characters.forEach(character => {
    request(character, (err, res, body) => {
      if (err) throw (err);
      console.log(JSON.parse(body).name);
    });
  });
});
