$(function() {
  var $input = $("#input-text"),
           inputs = "";

  $(".numbers button").on("click", function() {
    var character = $(this).text(),
        numberString = $input.val() + character;

    $input.val(numberString).focus();

  })

  $(".operations button.arithmetic").on("click", function() {
    var operation = $(this).text();
    inputs = $input.val() + operation;

    $input.val("").focus();
  });

  $(".operations button.result").on("click", function() {
    var result = eval(inputs + $input.val());

    $input.val(result).focus();
  });

  $(".operations button.clear").on("click", function() {
    inputs = "";
    $input.val("").focus();
  }); 


  $(document).on("keypress", function(e) {
  if(e.shiftKey && (e.which == 75)) {$input.val("")};
  });


  $(document).on("keypress", function(e) {
  if((e.which == 99)) {$input.val("")};
  });


  $(document).on("keypress", function(e) {
  if((e.which == 61)) {var result = eval(inputs + $input.val());
    $input.val(result)};
  });

 
});