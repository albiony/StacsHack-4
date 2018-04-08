$( document ).ready(function() {
    $("#submit").click(function(){
        var origin = $(this).siblings(".origin").val();
        var dest = $(this).siblings(".destination").val();
        var people = $(this).siblings(".passengers").val();
        alert("origin: " + origin + ", dest: " + dest + "people: " + people);
        //var data = {"routes":[[{"distance" : 1800000, "time": 110, "vehicle": "FLIGHT", "passengers": 3, "emission": 200}]]};
        //parseJson(data);
        $(function(){
    $.ajax("/calc/"+origin + "-" + dest + "-" + people, {
        success: function(data) {
          alert('Success!');
          var jsonData = JSON.parse(data);
          var x = parseJson(jsonData);
          fillDOM(x);
           
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
  for (var i = 0; i < routes.length; i++) {
    var route = routes[i];
    var totEmision = 0.0;
    for (var j = 0; j < route.length; j++) {
      var step = route[j];
      var vehicles = [];
        vehicles.push(step.vehicle);
        var emission = step.emission;
        totEmision += emission;
      returnValues.push([vehicles,totEmision]);
    }
  }
  return returnValues;
}

function fillDOM(list) {
    for (var route in list) {
        newli = document.createElement("li");
        newdiv = document.createElement("div");
        d = $(newdiv);
        newTxt = $("<b>Route option</b>")
        newul = document.createElement("us");
        nu = $(newul);
        d.append(newTxt);
        var vehicles = route[0];

        for (var veh in vehicles) {
            newsmallli = document.createElement("li");
            newveh = $("<b>" + veh + "</b>")
            newveh.appendTo(d);
            d.append(nu);
        }
        total = $("<p>" + route[1] + "</>")
        d.append(total)
        $("#list").append(d);
    }
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
