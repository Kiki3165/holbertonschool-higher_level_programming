#!/usr/bin/node

const axios = require('axios');
const movieId = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

axios.get(url)
  .then((response) => {
    console.log(response.data.title);
  })
  .catch((error) => {
    console.error(error);
  });
