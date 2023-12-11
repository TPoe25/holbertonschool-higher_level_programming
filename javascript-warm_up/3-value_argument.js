#!/usr/bin/node

// Retrieves the firsts command line arg
const argOne = process.argv[2];

// Checks if arg listed and prints message
if (typeof argOne === 'undefined') {
  console.log('No argument');
} else {
  console.log(argOne);
}
