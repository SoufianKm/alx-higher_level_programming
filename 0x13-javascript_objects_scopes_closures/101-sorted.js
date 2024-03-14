#!/usr/bin/node
/*
 * a script that imports a dictionary of occurrences by user
 * id and computes a dictionary of user ids by occurrence.
 */

const dictInput = require('./101-data').dict;
const newDict = {};

for (const key in dictInput) {
  const ocurr = dictInput[key];
  newDict[ocurr] = [];
  for (const keys in dictInput) {
    if (dictInput[keys] === ocurr) {
      newDict[ocurr].push(keys);
    }
  }
}
console.log(outDict);
