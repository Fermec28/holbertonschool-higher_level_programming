#!/usr/bin/node
exports.esrever = function (list) {
  const rever = [];
  for (let i = list.length - 1; i >= 0; i--) {
    rever.push(list[i]);
  }
  return rever;
};
