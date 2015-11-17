$(document).ready(function(){
  getLocation();
});


function getLocation() {
    if (navigator.geolocation) {
        var bla = navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}

function layerControl(map, base){

   var   ovi =   L.tileLayer('http://maptile.maps.svc.ovi.com/maptiler/maptile/newest/satellite.day/{z}/{x}/{y}/256/png8'),
    openstreets =  L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'),
    hiking =  L.tileLayer('http://osm.org.il/IsraelHiking/Tiles/{z}/{x}/{y}.png');

    var baseLayers = {
            "Basic Map": base,
			"OVI Satellite": ovi,
			"OpenStreet map": openstreets,
			"Israel Hiking Trails": hiking
		};
    L.control.layers(baseLayers).addTo(map);

}

function addingOldMap(map){


    var layer = L.tileLayer('http://46.101.211.183:3000/maps/tile/1/{z}/{x}/{y}.png', {
			maxZoom: 18,
		}).addTo(map);
    map.fitBounds(layer);

}

function showPosition(position) {
//  var map = L.map('map').setView([position.coords.latitude, position.coords.longitude], 16);
//  var marker = L.marker([position.coords.latitude, position.coords.longitude]).addTo(map);
//
//  base = L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
//      attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
//      maxZoom: 18,
//      id: 'nirgn975.cigmtjxyw000rc3knz02njkhn',
//      accessToken: 'pk.eyJ1IjoibmlyZ245NzUiLCJhIjoiY2lnbXRqeTcxMDAwdmx6a3RueGViemV0eCJ9.3wBhw04dxzXHfd56yUfufQ'
//  }).addTo(map);
//
//    layerControl(map, base)
//
//   	var layer2 = L.geoJson();
//	map.addLayer(layer2);
//	$.getJSON("{% url 'subway' %}", function (data2) {
//	layer2.addData(data2);
//	});
//
//	var fg = L.featureGroup(layer2);
//	map.fitBounds(layer2.getBounds())

}
