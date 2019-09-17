#!/usr/bin/node
const concurrences = process.argv[2];
if (concurrences && !isNaN(concurrences) && concurrences !== '') {
  for (let i = 0; i < parseInt(concurrences); i++) {
    console.log('C is fun');
  }
} else console.log('Missing number of occurrences');
