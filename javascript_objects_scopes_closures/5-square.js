#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    // calling the constructor of Rect class
    super(size, size);
  }
}

module.exports = Square;
