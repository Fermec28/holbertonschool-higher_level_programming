#!/usr/bin/node
function add (a, b) {
  if (!isNaN(a) && a !== '' && !isNaN(b) && b !== '') {
    return (parseInt(a) + parseInt(b));
  } else return (NaN);
}

const args = process.argv;
console.log(add(args[2], args[3]));
