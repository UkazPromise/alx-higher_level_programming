$(document).ready(function() {
  $.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",
    dataType: "json",
    success: function(data) {
      var movies = data.results;

      for (var i = 0; i < movies.length; i++) {
        $("#list_movies").append("<li>" + movies[i].title + "</li>");
      }
    },
    error: function(error) {
      console.error("Error fetching movie data:", error);
      $("#list_movies").text("Error: Could not retrieve movie titles.");
    }
  });
});
