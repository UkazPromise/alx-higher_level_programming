$(document).ready(function() {
  $("#btn_translate").click(function() {
    var languageCode = $("#language_code").val();

    $.ajax({
      url: "https://www.fourtonfish.com/hellosalut/hello/" + languageCode,
      dataType: "json",
      success: function(data) {
        $("#hello").text(data.hello);
      },
      error: function(error) {
        console.error("Error fetching translation data:", error);
        $("#hello").text("Error: Could not retrieve translation.");
      }
    });
  });
});
