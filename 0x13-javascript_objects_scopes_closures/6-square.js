#!/usr/bin/node
const Square5 = require('./5-square');

class Square extends Square5 {
  charPrint (c = 'X') {
    let toPrint = '';
    for (let i = 0; i < this.width; i++) {
      toPrint += c;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(toPrint);
    }
  }
}

module.exports = Square;
