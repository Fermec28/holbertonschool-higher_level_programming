$(document).ready(function () {
  $('#btn_translate').on('click', function () {
    const language = $('#language_code').val();
    $.ajax(
      {
        url: 'https://www.fourtonfish.com/hellosalut/',
        type: 'GET',
        data: { lang: language },
      })
      .done(function (data) {
        $('#hello').html(`<p> ${data.hello} </p>`);
      });
  });
});
