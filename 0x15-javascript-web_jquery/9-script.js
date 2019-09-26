$.ajax('https://fourtonfish.com/hellosalut/?lang=fr')
  .done(function (data) {
    $('#hello').html(`<p> ${data.hello} </p>`);
  });