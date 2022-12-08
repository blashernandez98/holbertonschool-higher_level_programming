#!/usr/bin/node

let big = 0;
const args = process.argv.slice(2);
if (args.length > 1) {
  args.forEach(e => {
    if (Number(e) > big) {
      big = Number(e);
    }
  });
}

console.log(big);
