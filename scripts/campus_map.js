var data;    
var campus_businesses;
d3.json("209_FinalProject_Data/food_businesses_by_campus.json", function(obj) {
  campus_businesses = obj;
});
function initMap() {
	d3.csv("209_FinalProject_Data/school_coords.csv", function(obj) {
	all_data = obj;
	$(".schoolbutton").click(function() {
		current_campus = $(this).attr('id');
		var longitude = $.grep(all_data, function(e){ return e.Campus == current_campus})[0].Long;
		lg = parseFloat(longitude);
		var latitude = $.grep(all_data, function(e){ return e.Campus == current_campus})[0].Lat;
		lt = parseFloat(latitude);
		var map = new google.maps.Map(document.getElementById('map'), {
			center: {lat: lg, lng: lt},//new google.maps.LatLng(latitude, longitude),
			zoom: 20
			});
		// var marker = new google.maps.Marker({
		// 	position: {lat: lg, lng: lt},
		// 	map: map
		// 	});
		campus_data = campus_businesses[current_campus];
		var bounds = new google.maps.LatLngBounds();
		if (campus_data !== undefined) {
			for (i in campus_data) {
				myLatLng = {lat: campus_data[i]['latitude'], lng: campus_data[i]['longitude']};
				var marker = new google.maps.Marker({
					position: myLatLng,
					map: map,
					icon: 'icons/' + current_campus + '.ico'
					});
				bounds.extend(marker.getPosition());
				google.maps.event.addListener(marker, 'click', (function(marker, i) {
					return function() {
						var infoWindow = new google.maps.InfoWindow();
						infoWindow.setContent(campus_data[i]['name']);
						infoWindow.open(map, marker);
						}	
					})(marker, i));
				}
			map.fitBounds(bounds);
		}
		});
	})
};
	