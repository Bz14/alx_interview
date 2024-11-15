#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const fetchData = (id) => {
  request(`https://swapi.dev/api/films/${id}/`, (err, res, body) => {
    if (err) {
      console.error('Error fetching film data:', err);
      return;
    }

    const character = JSON.parse(body);
    const characters = character.characters;

    characters.forEach((url) => {
      fetchActor(url);
    });
  });
};

const fetchActor = (url) => {
  request(url, (err, res, body) => {
    if (err) {
      console.error('Error fetching actor data:', err);
      return;
    }

    const actor = JSON.parse(body);
    console.log(actor.name);
  });
};

fetchData(id);
