#!/usr/bin/node
const fs = require('fs');

function readFile (path) {
  return (fs.readFileSync(path, (err, data) => {
    if (err) throw err;
    return (data);
  }));
}
fs.appendFile(process.argv[4], readFile(process.argv[2]), function (err) {
  if (err) throw err;
});
fs.appendFile(process.argv[4], readFile(process.argv[3]), function (err) {
  if (err) throw err;
});
