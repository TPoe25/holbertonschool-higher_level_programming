#!/usr/bin/node

// Get the first command-line argument
const x = process.argv[2];

// Check if the argument is not a valid number
if (isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  // Loop 'x' times and print "C is fun" in each iteration
  for (let i = 0; i < parseInt(x); i++) {
    console.log('C is fun');
  }
}