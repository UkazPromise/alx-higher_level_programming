$(document).ready(function() {
  $("#toggle_header").click(function() {
    var currentClass = $("header").attr("class");

    if (currentClass === "red") {
      $("header").removeClass("red").addClass("green");
    } else {
      $("header").removeClass("green").addClass("red");
    }
  });
});
