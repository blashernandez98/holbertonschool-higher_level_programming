#!/usr/bin/node

let printed = 0;

exports.logMe = function logMe (item) {
  console.log(`${printed++}: ${item}`);
};
