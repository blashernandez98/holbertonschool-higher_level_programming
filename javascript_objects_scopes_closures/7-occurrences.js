#!/usr/bin/node

exports.nbOccurrences = function (list, search) {
  let res = 0;
  list.forEach(element => {
    if (element === search) {
      res++;
    }
  });

  return res;
};
