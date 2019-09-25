#!/usr/bin/node
const request = require('request');
const URI = process.argv[2];
request(URI, function (error, response, body) {
  if (error) console.log(error);
  let list = JSON.parse(body).results;
  list = list.map((x) => x.characters);
  list = list.reduce((accu, current) => [...accu, ...current]);
  console.log(list.filter(x => x.includes('/18/')).length);
});
