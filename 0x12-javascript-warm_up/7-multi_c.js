#!/usr/bin/node
// Include process module;
const arg = process.argv[2];
for (let i = 0; i < arg; i++) {
  if (isNaN(arg)) {
    console.log('Missing number of occurrences');
  } else {
    console.log('C is fun');
  }
}
