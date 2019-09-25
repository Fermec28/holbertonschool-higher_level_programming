#!/usr/bin/node
const request = require('request');
const URI = `https://swapi.co/api/films/${process.argv[2]}`;

function doRequest (url) {
  return new Promise(function (resolve, reject) {
    try {
      request(url, function (error, res, body) {
        if (error) console.log(error);
        resolve(body);
      });
    } catch (err) {
      reject(err);
    }
  });
}

request(URI, function (error, res, body) {
  if (error) console.log(error);
  const characters = JSON.parse(body).characters;
  getcharacter(characters);
});

const getcharacter = async (characters) => {
  for (const chaar of characters) {
    const data = await doRequest(chaar);
    console.log(JSON.parse(data).name);
  }
};
