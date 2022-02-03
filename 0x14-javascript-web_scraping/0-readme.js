#!/usr/bin/node
/* Script that reads and prints the content of a file */

const fs = require('fs');
const argu = process.argv[2];

fs.readFile(argu, 'utf8', function (err, data) {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
