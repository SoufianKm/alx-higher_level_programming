#!/usr/bin/node
/*
 * a function that increments and calls a function.
 * The function must be visible from outside
 */

exports.addMeMaybe = function (number, theFunction) {
  theFunction(++number);
};
