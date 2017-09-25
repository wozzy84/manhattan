$(function() {
  var $input = $("#input-text"),
      inputs = "";

  $(".numbers button").on("click", function() {
    var character = $(this).text(),
        numberString = $input.val() + character;

    $input.val(numberString);
  })

  $(".operations button.arithmetic").on("click", function() {
    var operation = $(this).text();
    inputs = $input.val() + operation;

    $input.val("");
  });

  $(".operations button.result").on("click", function() {
    var result = eval(inputs + $input.val());

    $input.val(result);
  });

  $(".operations button.clear").on("click", function() {
    inputs = "";
    $input.val("");
  });
});
