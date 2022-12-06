#!/usr/bin/node

const argv = process.argv.length;

if (argv === 2) {
  console.log('No argument');
}
if (argv === 3) {
  console.log('Argument found');
}
if (argv > 3) {
  console.log('Arguments found');
}
