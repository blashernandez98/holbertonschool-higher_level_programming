#!/usr/bin/node

let arg = Number(process.argv[2]);

if (isNaN(arg)) {
  console.log('Missing number of occurrences');
}

while (arg-- > 0) {
  console.log('C is fun');
}
