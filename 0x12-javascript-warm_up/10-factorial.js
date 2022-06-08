#!/usr/bin/node
// program to find the factorial of a number;
const x = process.argv[2];
function factorial (x) {
  if (isNaN(x) || x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
console.log(factorial(parseInt(x)));
