$(function() {
  $("#plus").on("click", function() {
    var firstNumber = Number($("#first").val());
    var secondNumber = Number($("#second").val());
    $("#wynik").text(firstNumber + secondNumber);
  });
});
