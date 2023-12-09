#!/usr/bin/node

// Defines the add func
function add (a, b) {
  return a + b;
}

// gets the 1st and 2nd ints from cmdline args
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

// Checking if both args are valid ints
if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  // Calls add function and prints result
  console.log(add(num1, num2));
}
