#!/usr/bin/node

const urlPath = process.argv[2];
const request = require('request');

request(urlPath, function (err, res, body) {
  if (err) throw (err);
  console.log(`code: ${res.statusCode}`);
});
