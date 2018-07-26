// Make life easier to reload
function refreshPage() {
  window.location.reload(true);
}

// Bind refresh button to menu
$("#nav_refresh").click(refreshPage);

// Refresh the page every 5 minutes
$(document).ready(function () {
  setInterval(refreshPage, 300000);
});
