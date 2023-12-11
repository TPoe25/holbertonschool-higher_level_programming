#!/usr/bin/node

// Retrieves the number of command line args
const numArgs = process.argv.length;

// Checks the number of args and prints message
if (numArgs === 2) {
  console.log('No argument');
} else if (numArgs === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
