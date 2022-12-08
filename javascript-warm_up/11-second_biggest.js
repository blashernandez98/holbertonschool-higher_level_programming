#!/usr/bin/node

let big = 0;
let second = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.forEach(e => {
    e = Number(e);
    if (e > big) {
      second = big;
      big = e;
    } else if (e > second) {
      second = e;
    }
  });
}

console.log(second);
