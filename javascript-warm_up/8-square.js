#!/usr/bin/node

// Get the size of square from cmd line arguments
const squareSize = parseInt(process.argv[2]);

// Looks to see if arg is missing or not valid number
if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  // Looping thru and printing sq of size x
  for (let i = 0; i < parseInt(squareSize); i++) {
    console.log('X'.repeat(squareSize));
  }
}
