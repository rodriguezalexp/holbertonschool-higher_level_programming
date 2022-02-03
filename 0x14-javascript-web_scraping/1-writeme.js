#!/usr/bin/node
/* Script that reads and prints the content of a file */
const fs = require('fs');

fs.writeFileSync(process.argv[2], process.argv[3]);