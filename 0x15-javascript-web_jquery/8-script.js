$.ajax('https://swapi.co/api/films/?format=json')
  .done(function (data) {
    data.results.forEach(function (movie) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    });
  });
