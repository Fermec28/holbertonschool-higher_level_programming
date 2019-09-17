#!/usr/bin/node
function factorial (number) {
  if (!isNaN(number) && number !== '') {
    if (parseInt(number) === 0 || parseInt(number) === 1) return (1);
    else return (parseInt(number) * factorial(parseInt(number) - 1));
  } else return (1);
}

const args = process.argv;
console.log(factorial(args[2]));
