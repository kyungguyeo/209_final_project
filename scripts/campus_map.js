var data;    
var campus_businesses;
var highest_reviews;
var myStyle = [
  {
    featureType: "poi",
    elementType: "labels",
    stylers: [
      { visibility: "off" }
    ]
  }
];
d3.json("209_FinalProject_Data/food_businesses_by_campus.json", function(obj) {
  campus_businesses = obj;
});
d3.json("209_FinalProject_Data/highest_reviews_by_business.json", function(obj) {
  highest_reviews = obj;
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
			mapTypeControlOptions: {
			mapTypeIds: ['mystyle', google.maps.MapTypeId.ROADMAP, google.maps.MapTypeId.TERRAIN]
			},
			center: {lat: lg, lng: lt},//new google.maps.LatLng(latitude, longitude),
			zoom: 12,
			mapTypeId: 'mystyle'
			});
		map.mapTypes.set('mystyle', new google.maps.StyledMapType(myStyle, { name: 'My Style' }));
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
				var infoWindow = new google.maps.InfoWindow();
				google.maps.event.addListener(marker, 'click', (function(marker, i) {
					return function() {
						$("#comments-panel").show();
						biz_id = campus_data[i]['business_id'];
						infoWindow.setContent(campus_data[i]['name']);
						infoWindow.open(map, marker);
						$('.biz-title').remove();
						$('.biz-photo').remove();
						$("#biz").prepend("<img src=" + campus_data[i]["photo_url"] + " style='width:60%;height:25%' class='biz-photo'>");
						$("#business").prepend("<h3 class='biz-title'>" + campus_data[i]["name"] + "</h3>");
						$(".review-count").html("<h3> Reviews by Star Rating: <small>" + campus_data[i]["review_count"] + " reviews</small></h3>");
						biz_revs = highest_reviews[biz_id];
						count = 1; //for getting the right panel id
						for (i in biz_revs) {
							review_text = biz_revs[i]['text'];
							vote_laugh = biz_revs[i]['votes']['funny'];
							vote_cool = biz_revs[i]['votes']['cool'];
							vote_useful = biz_revs[i]['votes']['useful'];
							stars = biz_revs[i]['stars'];
							date = biz_revs[i]['date'];
							$('#panelbody' + count).text(review_text);
							$('#laugh' + count).html("<img src='images/laugh.png' style='width:30px;height:30px' title='funny'>" + vote_laugh);
							$('#cool' + count).html("<img src='images/cool.png' style='width:30px;height:30px' title='cool'>" + vote_cool);
							$('#useful' + count).html("<img src='images/useful.png' style='width:30px;height:30px' title='useful'>" + vote_useful);
							$("#date" + count).text(date)
							for (i=5; i>5-stars; i--) {
								$("." + count + "star" + i).css('opacity','1');
							}
							count++;
							}
						$("html, body").scrollTop($('#page3').offset().top);
						}
					})(marker, i));
				}
			map.fitBounds(bounds);
		}
		});
	})
};
	