var id;
var songs;
var $refresh;
var $code;

$(document).ready(function(){
	$('#setlist').hide();
	$('#venue').hide();
	$('#spotify').hide();
	$('#search').hide();

	$(document).ajaxStart(function () {
        $("#loading").show();
    }).ajaxStop(function () {
        $("#loading").hide();
    });

		window.addEventListener("message", function(event) {
	        console.log("received message " + event.data);
	    }, false);
});


function searchConcert() {
	$('#setlist').hide();
	$('#spotify').hide();
	$('#venue').hide();

	var artist = 'artist=' + $('#artist').val();
	var city = '&city=' + $('#city').val();
	var year = '&year=' + $("#year").val();

	$.getJSON('concerts.py?' + artist + city + year,
			function(data) {
				$id = data['id'];
				$songs = data['songs'];
				$venues = data['venues'];

				var new_HTML = [];

				if (data['venue'] == false){

					new_HTML.push(	'<div class="card-body">',
									'<h2 class="card-title">Setlist</h2>',
									'<ol>');

					$.each($songs, function(index, value) {
						new_HTML.push('<li>' + value + '</span>');
					});
					new_HTML.push(	'</ol>',
									'<div class="float-right"><button onClick="spotify()" class="btn btn-dark"> Next </button></div>',
									'</div>');

					$('#setlist_content').html(new_HTML.join(""));
					$('#setlist').show();

				} else {

					new_HTML.push(	'<div class="card-body">',
									'<h2 class="card-title">Venue</h2>' );

					$.each($venues, function(index, value) {
						new_HTML.push(
							'<div class="form-check">',
							'<input type="radio" name="venues" value="' + value[0] + '"></input>',
							'<label class="form-check-label">' + value[1] + '</label>',
							'</div>' );
					});

					new_HTML.push(
						'<div class="text-right searchbtn"><button onClick="searchById()" class="btn btn-dark"> Next </button></div>',
						'</div>');

					$('#venue_content').html(new_HTML.join(""));
					$('#venue').show();
				}
			}
	);
};


function searchById() {
	var radioGroup = document.getElementsByName("venues");
	for (var i=0; i<radioGroup.length; i++)  {
		    if (radioGroup[i].checked)  {
			var id = radioGroup[i].value;
			} };

	$.getJSON('concerts.py?id=' + id,
			function(data) {
				$id = data['id'];
				$songs = data['songs'];
				$venues = data['venues'];

				var new_HTML = [];

				if (data['venue'] == false){

					new_HTML.push(	'<div class="card-body">',
									'<h2 class="card-title">Setlist</h2>',
									'<ol>');

					$.each($songs, function(index, value) {
						new_HTML.push('<li>' + value + '</li>');
					});
					new_HTML.push(	'</ol>',
									'<div class="float-right"><button onClick="spotify()" class="btn btn-dark"> Next </button></div>',
									'</div>');

					$('#setlist_content').html(new_HTML.join(""));
					$('#setlist').show();

				}
			});
}

function spotify() {
	if ($refresh == undefined) {
		var $url;
		$.getJSON('spotify.py?id=' + $id + '&code=' + $code,
				function(data){
					$refresh = data['refresh'];
					$url = data['url'];
					$('#spotify_content').html(
			'<iframe src="https://open.spotify.com/embed?uri=' + $url + '&theme=white" height="500" frameborder="0" allowtransparency="true"></iframe>'
			);
		$('#spotify').show();
				});
		} else {
		$.getJSON('spotify.py?id=' + $id + '&refresh=' + $refresh,
				function(data){
					$url = data['url'];
					$('#spotify_content').html(
			'<iframe src="https://open.spotify.com/embed?uri=' + $url + '&theme=white" height="500" frameborder="0" allowtransparency="true"></iframe>'
			);
		$('#spotify').show();
				});
		}
}

function login() {
	var w = window.open('https://accounts.spotify.com/authorize/?client_id=ad25342922164745a3d5b9363c3d3f75&response_type=code&redirect_uri=http%3A%2F%2Fjrloaiza.me%2Fconcerts%2Fcallback.php&scope=playlist-modify-private+playlist-read-private',
									"_blank",
									"status=1, toolbar=0,resizable=0, width=600, height=700");
}

function onSpotifyAuth(str) {
	$code = str;

	if ($code != "") {
		$('#login').hide();
		$('#search').show();
	}
}
