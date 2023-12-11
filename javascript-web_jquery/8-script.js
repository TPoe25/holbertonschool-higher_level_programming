// Import jQuery
import $ from 'jquery';

$(document).ready(function () {
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(apiUrl, function (data) {
    const movies = data.results;
    const listMoviesElement = $('#list_movies');
    movies.forEach(function (movie) {
      const listItem = $('<li>').text(movie.title);
      listMoviesElement.append(listItem);
    });
  });
});
