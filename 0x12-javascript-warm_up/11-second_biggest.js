#!/usr/bin/node
let x = 0;
const arg = process.argv.slice(2);
if (arg.length > 1) {
  arg.sort();
  x = arg[arg.length - 2];
}
console.log(x);
