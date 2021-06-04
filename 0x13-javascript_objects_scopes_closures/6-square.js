#!/usr/bin/node

const AlphaSquare = require('./5-square');

class Square extends AlphaSquare {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.width; i++) {
       console.log(`${c}`.repeat(this.height));
      }
    } else {
       this.print();
     }
  }
}
module.exports = Square;
