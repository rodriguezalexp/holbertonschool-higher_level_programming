#!/usr/bin/node
/* Script that write a string to a file */
const fs = require('fs');

fs.writeFileSync(process.argv[2], process.argv[3]);
