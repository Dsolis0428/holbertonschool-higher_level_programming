#!/usr/bin/node
module.exports = class Rectangle {
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
	   const exhange = this.width;
	   this.width = this.height;
	   this.height = exchange;
   }
   double () {
	   this.width *= 2;
	   this.hieght *= 2;
   }
}
