$(document).ready(function() {
  // Translate on button click
  $("#btn_translate").click(function() {
    fetchTranslation();
  });

  // Translate on Enter key press in language code input
  $("#language_code").keypress(function(event) {
    if (event.which === 13) { // Check if Enter key is pressed (keyCode 13)
      fetchTranslation();
    }
  });

  function fetchTranslation() {
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
  }
});
