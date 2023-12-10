#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // creates empty object if w or h is >= 0
      return {};
    }

    // Initalizing instance of width and height w/ their values
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
