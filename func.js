function drawDOM(list) {
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