#!/usr/bin/node
/*
 * a script that prints My number: <first argument converted in integer>
 * if the first argument can be converted to an integer:
 *    If the argument can’t be converted to an integer, print “Not a number”
 */
const nbr = process.argv[2];
console.log(parseInt(nbr) ? 'My number: ' + parseInt(nbr) : 'Not a number');
