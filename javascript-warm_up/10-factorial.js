#!/usr/bin/node

// Defines the factory function
function factorial (n) {
  // Base case: factorial of 0 is 1
  if (n <= 0) {
    return 1;
  }

  // Iterative case for factorial using loop
  let result = 1;
  for (let i = 1; i <= n; i++) {
    result *= i;
  }

  return result;
}

// Gets the int from the cmdline argument
const num = parseInt(process.argv[2]);

// Compute and print factorial
console.log(factorial(num));
