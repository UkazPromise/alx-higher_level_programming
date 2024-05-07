$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    dataType: "json",
    success: function(data) {
      $("#character").text(data.name);
    },
    error: function(error) {
      console.error("Error fetching character data:", error);
      $("#character").text("Error: Could not retrieve character name.");
    }
  });
});
