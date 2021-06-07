#!/usr/bin/node

exports.callMeMoby = function (n, thefunction) {
  let x = 0;

  for (; x < n; x++) {
      thefunction();
    }
};
