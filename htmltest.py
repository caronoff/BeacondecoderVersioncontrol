google_map =                 '''<!DOCTYPE html>
        <html>
          <head>
            <meta name="viewport" content="initial-scale=1.0, user-scalable=no">
            <meta charset="utf-8">
            <title>Simple markers</title>
            <style>
              html, body, #map-canvas {
                height: 100%;
                width: 100%
                margin: 0px;
                padding: 0px
              }
            </style>
            <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBw4IpZdm6D7ob00fF9F9TjuZ2Eeif9QtE"></script>
            <script>           

                


                 function Marker(Lat,Lng) {
                    var myLatLng = {lat: Lat, lng: Lng}                  
                     
                    var map = new google.maps.Map(document.getElementById('map-canvas'),{
                    zoom: 8,
                    minZoom: 2,
                    center: myLatLng
                    }); 
                    
                    var marker = new google.maps.Marker({
                    position: myLatLng,
                    map: map,
                    title: 'Hello World!'});}
        
            </script>
          </head>
          <body>
            <div id="map-canvas"></div>
          </body>
        </html> '''


blank =                 '''<!DOCTYPE html>
        <html>
       <body>

        <h1>No Map</h1>

        <p>No Map Data.</p>

        </body>
        </html> '''
