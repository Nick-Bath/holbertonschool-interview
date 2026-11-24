#!/usr/bin/node

const request = require('request');

const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

function get (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        return reject(error);
      }
      resolve(JSON.parse(body));
    });
  });
}

async function printChars () {
  try {
    const data = await get(url);
    if (!data.characters) {
      console.error('Film not found');
      return;
    }
    for (const api of data.characters) {
      const char = await get(api);
      console.log(char.name);
    }
  } catch (error) {
    console.error(error);
  }
}

printChars();
