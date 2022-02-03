#!/usr/bin/node
/* script that prints the title of a Star Wars movie from request */

const request = require('request');
const url = process.argv[2];
const Antilles = 'https://swapi-api.hbtn.io/api/people/18/';

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }

  const n_objs = JSON.parse(body).results;
  let d = 0;
  for (const i in n_objs) {
    const characters = n_objs[i].characters;
    for (const idx in characters) {
      if (characters[idx] === Antilles) {
        d++;
      }
    }
  }
  console.log(d);
});
