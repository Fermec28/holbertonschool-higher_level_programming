#!/usr/bin/node
const numberArguments = process.argv.length;
if (numberArguments === 2) console.log('No argument');
else if (numberArguments === 3) console.log('Argument found');
else console.log('Arguments found');
