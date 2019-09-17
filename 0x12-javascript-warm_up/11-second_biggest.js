#!/usr/bin/node
const args = process.argv.slice(2).sort((a, b) => b - a);
if (args[1] && args[1] !== '') console.log(args[1]);
else console.log(0);
