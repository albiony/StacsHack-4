$(document).ready(function() {
    $("#submit").click(function(){
        var origin = $(this).siblings(".origin").val()
        var dest = $(this).siblings(".destination").val()
        var people = $(this).siblings(".passengers").val()
        alert("origin: " + origin + ", dest: " + dest + "people: " + people)
        ajax({
            type: 'POST',
            url: "server.js",
            data: origin + "-" + dest + "-" + people,
            success: function(response) {
                alert("Submitted form");
                alert("Data: " + data)
            },
            error: function() {
                alert("There was an error while submitting form");
            }
        });
    });
});