#!/usr/bin/node
const toNumber = process.argv[2];
if (!isNaN(toNumber) && toNumber !== '') {
  console.log(`My number: ${parseInt(toNumber)}`);
} else console.log('Not a number');
