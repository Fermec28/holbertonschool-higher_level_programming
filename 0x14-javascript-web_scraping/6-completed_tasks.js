#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  let list = JSON.parse(body).filter((x) => x.completed);
  list = list.reduce((accu, current) => {
    accu[current.userId] = accu[current.userId] + 1 || 1;
    return accu;
  }, {});
  console.log(list);
});
