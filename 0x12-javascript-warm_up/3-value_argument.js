#!/usr/bin/node
'use strict';
const len = process.argv.slice(2);

if (len.length < 1) {
  console.log('No argument');
} else {
  console.log(len);
}
