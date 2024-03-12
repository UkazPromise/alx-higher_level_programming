#!/usr/bin/node

// Define the callMeMoby function
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
