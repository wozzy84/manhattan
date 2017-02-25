$(function() {
  $("#search").on("click", function(event) {
    var inputValue = $("#input-text").val();
    event.preventDefault();

    $.get("https://restcountries.eu/rest/v2/name/" + inputValue)
      .done(function(data) {
        console.log(data)
      });
  });
})
