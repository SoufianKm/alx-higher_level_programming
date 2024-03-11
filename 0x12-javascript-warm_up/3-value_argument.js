#!/usr/bin/node
/*
 * a script that prints the first argument passed to it:
 *    If no arguments are passed to the script, print “No argument”
 */

const arg = process.argv[2];
console.log(arg === undefined ? 'No argument' : arg);
