// Base class for javascript functions we need throughout the app

function getWeather() {
  $.getJSON("/static/data/forecast.json", function(data) {
    $("#cell1").html('Currently:<br/>' + data.currently.summary);
    $("#cell2").html('Temperature:<br>' + data.currently.temperature + 'F');
    $("#cell3").html('Humidity:<br>' + data.currently.humidity * 100 + '%');
  });
}


// Kick off the scripts
weather = getWeather();
