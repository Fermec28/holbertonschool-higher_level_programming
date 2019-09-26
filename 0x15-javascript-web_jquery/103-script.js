const lanCall = function () {
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
}

$(document).ready(function () {
  $('#btn_translate').on('click', lanCall);
  $('INPUT#language_code').keyup(function (e) {
    if (e.which === 13) {
      lanCall();
    }
  });
});