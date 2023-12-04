#!/usr/bin/node

// Retrieves the 1st and 2nd command line arg
let arg1 = process.argv[2];
let arg2 = process.argv[3];

// Checks args and prints message
if (typeof arg1 === 'undefined') {
  arg1 = 'undefined';
}

if (typeof arg2 === 'undefined') {
  arg2 = 'undefined';
}

// Prints format for output
console.log(`${arg1} is ${arg2}`);
