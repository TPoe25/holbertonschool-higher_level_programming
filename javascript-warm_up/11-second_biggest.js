#!/usr/bin/node

// Gets the cmdline args and makes them ints
const numbs = process.argv.slice(2).map(Number);

// if no args or only 1 listed, prints 0
if (numbs.length <= 1) {
  console.log(0);
} else {
  // arranges array of numbs in desc order
  const descNumbs = numbs.sort((a, b) => b - a);

  // Prints the 2nd largest nunber
  console.log(descNumbs[1]);
}
