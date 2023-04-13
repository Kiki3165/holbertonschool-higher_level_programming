#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
  print () {
    let row = '';
    for (let i = 0; i < this.width; i++) {
      row += 'X';
    }
    for (let j = 0; j < this.height; j++) {
      console.log(row);
    }
  }
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

  class Square extends Rectangle {
    constructor(size) {
      super(size, size);
    }
  }

module.exports = Rectangle;
