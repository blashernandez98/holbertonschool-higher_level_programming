#!/usr/bin/node

const urlPath = process.argv[2];
const searchCharacter = 'https://swapi-api.hbtn.io/api/people/18/';
const request = require('request');
let count = 0;

request(urlPath, function (err, res, body) {
  if (err) throw (err);

  const movies = JSON.parse(body);
  movies.results.forEach(movie => {
    if (movie.characters.includes(searchCharacter)) {
      count++;
    }
  });

  console.log(count);
});
