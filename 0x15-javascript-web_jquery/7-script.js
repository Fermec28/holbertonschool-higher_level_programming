$.ajax('https://swapi.co/api/people/5/?format=json')
  .done(function (data) {
    $('DIV#character').text(data.name);
  });
