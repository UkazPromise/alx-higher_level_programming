#!/usr/bin/node

// Define the addMeMaybe function
exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
