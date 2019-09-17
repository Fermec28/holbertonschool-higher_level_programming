#!/usr/bin/node
const concurrences = process.argv[2];
if (concurrences && !isNaN(concurrences) && concurrences !== '') {
  let prompt = '';
  for (let i = 0; i < parseInt(concurrences); i++) {
    prompt += 'X';
  }
  for (let i = 0; i < parseInt(concurrences); i++) {
    console.log(prompt);
  }
} else console.log('Missing size');
