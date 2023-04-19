#!/usr/bin/node

$(document).ready(function() {
    $.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
      const titles = data.results.map(function(movie) {
        return `<li>${movie.title}</li>`;
      });
      $('#list_movies').html(titles.join(''));
    });
  });
