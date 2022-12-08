#!/usr/bin/node

exports.callMeMoby = function(n, f){
    for (; n > 0; n--) {
      f();
    }
}