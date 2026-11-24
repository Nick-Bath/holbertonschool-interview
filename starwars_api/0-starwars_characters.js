#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

function get (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      resolve(JSON.parse(body));
    });
  });
}

async function printChars () {
  const data = await get(url);
  for (const api of data.characters) {
    const char = await get(api);
    console.log(char.name);
  }
}

printChars();
