window.onload = function() {
    console.log("Footer loading.");
    var version = "3.0.3";
    var date = "1/6/2017";
    document.getElementById("version").innerHTML = version;
    document.getElementById("date").innerHTML = date;
    var url = window.location.href;
    console.log(url);
    if ((url).includes("localhost")) {
        console.log("Modifying form elements.");
        for (var i = 0; i < document.forms.length; i++) {
            var action = document.forms[i].action.split("/");
            console.log(action);
            action.splice(3,1);
            console.log(action);
            document.forms[i].action = action.join("/");
        }
    }
}
