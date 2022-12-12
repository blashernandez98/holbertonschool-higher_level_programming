#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    let aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }

}

module.exports = Rectangle;
