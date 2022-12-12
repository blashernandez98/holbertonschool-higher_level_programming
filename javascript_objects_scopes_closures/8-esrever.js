#!/usr/bin/node

function esrever (list) {
  if (!list) {
    return list;
  }
  let i = list.length - 1;
  const rev = [];
  for (; i >= 0; i--) {
    rev.push(list[i]);
  }
  return rev;
}

exports.esrever = esrever;
