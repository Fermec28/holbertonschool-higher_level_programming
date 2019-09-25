#!/usr/bin/node
const request = require('request');
const URI = `http://swapi.co/api/films/${process.argv[2]}`;
request(URI, function (error, response, body) {
  if (error) console.log(error);
  console.log(JSON.parse(body).title);
});
