$( document ).ready(function() {
    $("#submit").click(function(){
        var origin = $(this).siblings(".origin").val();
        var dest = $(this).siblings(".destination").val();
        var people = $(this).siblings(".passengers").val();
        alert("origin: " + origin + ", dest: " + dest + "people: " + people);
        $(function(){
    $.ajax("calc/"+origin + "-" + dest + "-" + people, {
        success: function(data) {
          var data = {"routes":[[{"distance" : 39, "time": 110, "vehicle": "FLIGHT", "passengers": 3, "emission": 200}]]};
          alert('Success!');
          var jsonData = JSON.parse(data);
          parseJson(jsonData);
        },
        error: function() {
            alert("There was an error while submitting form");
        }
    });
  });
});

function parseJson(json) {
  var routes = json.routes;
  var returnValues=[];
  for (var i = 0; i < routes.size(); i++) {
    var route = routes[i];
    for (var j = 0; j < route.size(); j++) {
      var step = route[j];
      var vehicles = [];
      var totEmision = 0.0;
      for (var k = 0; k < step.size(); k++) {
        vehicles.push(step[k].vehicle);
        var emission = step[k].emission;
        totEmision = totEmision + emission;
        //var dist = step[k].distance;
        //var pas = step[k].passengers;
        returnValues.push([dist, time, veh, pas, emission]);
      }
    }
  }
}

function fillDOM(vehicles, emission) {

}


        /*&.ajax({
            type: 'getElementsByClassName('className')',
            url: "server.js",
            data: origin + "-" + dest + "-" + people,
            success: function(response) {
                alert("Submitted form");
                alert("Data: " + data)
            },
            error: function() {
                alert("There was an error while submitting form");
            }
        });*/
});
