#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // if w or h >= to 0 creates empt obj
      return {};
    }

    // Initalizing atts witdh and height w/ values
    this.width = w;
    this.height = h;
  }

  print () {
    // making loop to print X for each row & column
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
