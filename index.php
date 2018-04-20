<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />
    <title>Setlist to Spotify - J.R. Loaiza</title>
    <script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <link rel="stylesheet" type="text/css" href="style.css">

    <script type='text/javascript' src="main.js"></script>

</head>

<body>
<div id="title-container">
            <div id="title-content" class="align-middle">
                <a href="/concerts/"><img src="Spotify_Icon_RGB_White.png"></a>
                <h1>Setlist to Spotify </h1>
                <a href="about.php" class="float-right align-middle">About</a>
            </div>
        </div>
    <div class="main container-fluid">

        <div id="login" class="text-center" style="padding-top: 50px;">
            <button onClick="login()" class="btn btn-dark">Authorize the app to start!</button>
        </div>

        <div class="row jumbotron">

            <div class="col-md-6 col-lg-4 col-xl-3" id="col1">

                <div class="card" id="search">

                    <h2 class="card-header"> Search </h2>
                    <div class="card-body">

                        <div class="form-row">
                            <label class="col-3" for="artist"> Artist: </label>
                            <div class="col-9"><input type="text" id="artist"></div>
                        </div>

                        <div class="form-row">
                            <label class="col-3" for="city"> City: </label>
                            <div class="col-9"><input type="text" id="city"></div>
                        </div>

                        <div class="form-row">
                            <label class="col-3"> Year: </label>
                            <div class="col-9"><input type="text" id="year"></div>
                        </div>

                        <div class="float-right searchbtn">
														<button onClick="searchConcert()" class="btn btn-dark"> Next </button>
												</div>

                    </div>
                </div>

                <div id="venue">
                    <div id="venue_content" class="card">
                    </div>
                </div>
            </div>

            <div class="col-md-6 col-lg-5 col-xl-5" id="setlist">
                <div id="setlist_content" class="card">
                </div>
            </div>

            <div class="col-md-6 col-lg-5 col-xl-4" id="spotify">
                <div id="spotify_content" class="card">
                </div>
            </div>
        </div>



        <div class="footer">
            <button id="loading" class="btn btn-secondary fixed-bottom float-right" style="display:none">Loading...</button>
        </div>
    </div>
</body>

</html>
