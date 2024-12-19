#!/usr/bin/node
/* a class Square that inherits from Square of 5-square.js */

module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        console.log(c.repeat(this.width));
      }
    }
  }
};
