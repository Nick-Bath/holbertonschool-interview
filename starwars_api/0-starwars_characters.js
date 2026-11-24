#!/usr/bin/node

async function getData (id) {
  try {
    const response = await fetch(`https://swapi-api.hbtn.io/api/films/${id}`);

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();

    for (const url of data.characters) {
      const res = await fetch(url);
      const character = await res.json();
      console.log(character.name);
    }
  } catch (error) {
    console.error('Fetch failed:', error);
  }
}

getData(process.argv[2]);
