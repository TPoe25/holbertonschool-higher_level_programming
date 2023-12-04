#!/usr/bin/node

// Retrieves the first command line arg
const arg = process.argv[2];

// Change the arg to an integer
const num = parseInt(arg);

// Checks in change was successful and prints message
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
