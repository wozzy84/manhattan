$(function() {
  var $inputText = $("#input-text"),
      endpoint = "https://restcountries.eu/rest/v2/name/",
      template = $("#country-template").html(),
      $results = $("#results");


  $("#search").on("submit", function(event) {
    var inputValue = $inputText.val(),
        request;

    event.preventDefault();

    request = $.get(endpoint + inputValue)
      .done(function(data) {
        var i;

        $results.html("");
        for(i = 0; i < data.length; i += 1) {
          html = Mustache.to_html(template, data[i]);
          if(i === 0) {
            html = $(html).addClass("is-active");
          }
          $results.append(html);
        }
      })
      .done(function() {
        $results.foundation();
      });
  });
})
