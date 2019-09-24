#!/usr/bin/node

function constructor () {
  let times = 0;
  return function (item) {
    console.log(`${times++} ${item}`);
  };
}

exports.logMe = constructor();
