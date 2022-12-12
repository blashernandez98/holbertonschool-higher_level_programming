#!/usr/bin/node

function nbOccurences (list, search) {
  let res = 0;
  list.forEach(element => {
    if (element === search) {
      res++;
    }
  });

  return res;
}

exports.nbOccurences = nbOccurences;
