$(document).ready(function(){
  getLocation();
});


function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}


function showPosition(position) {
  var map = L.map('map').setView([position.coords.latitude, position.coords.longitude], 16);
  var marker = L.marker([position.coords.latitude, position.coords.longitude]).addTo(map);

  L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
      attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
      maxZoom: 18,
      id: 'nirgn975.cigmtjxyw000rc3knz02njkhn',
      accessToken: 'pk.eyJ1IjoibmlyZ245NzUiLCJhIjoiY2lnbXRqeTcxMDAwdmx6a3RueGViemV0eCJ9.3wBhw04dxzXHfd56yUfufQ'
  }).addTo(map);


<<<<<<< HEAD:viewer-app/viewer/static/js/leaflet_map.js
  layer = L.tileLayer('http://46.101.211.183:3000/maps/tile/1/{z}/{x}/{y}.png?access_token={accessToken}', {
      attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
      maxZoom: 18,
      id: 'nirgn975.cigmtjxyw000rc3knz02njkhn',
      accessToken: 'pk.eyJ1IjoibmlyZ245NzUiLCJhIjoiY2lnbXRqeTcxMDAwdmx6a3RueGViemV0eCJ9.3wBhw04dxzXHfd56yUfufQ'
  }).addTo(map);
=======
   var ovi =   L.tileLayer('http://maptile.maps.svc.ovi.com/maptiler/maptile/newest/satellite.day/{z}/{x}/{y}/256/png8'),
        openstreets =  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'),
        hiking =  L.tileLayer('http://osm.org.il/IsraelHiking/Tiles/{z}/{x}/{y}.png');

    var baseLayers = {
			"OVI Satellite": ovi,
			"OpenStreet map": openstreets,
			"Israel Hiking Trails": hiking
		};
    L.control.layers(baseLayers).addTo(map);

>>>>>>> 67b25a11b70f3ab54a9ee05b91889631affc4490:viewer/static/js/leaflet_map.js
}
