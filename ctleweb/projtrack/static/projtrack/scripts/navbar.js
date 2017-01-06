window.onload = function() {

    var version = "3.0.2";
    var date = "1/6/2017";

    console.log("Navbar loading.");
    var bar = "<table><th>";
    bar += "<td><button onclick='home()'>Home</button></td>";
    bar += "<td><button onclick='my_projects()'>My Projects</button></td>";
    bar += "<td><button onclick='add_project()'>Add Project</button></td>";
    bar += "<td><button onclick='all_projects()'>All Projects</button></td>";
    bar += "<td><button onclick='logout()'>Sign Out</button></td>"
    bar += "</th></table>";
    document.getElementById("navbar").innerHTML = bar;
    document.getElementById("version").innerHTML = version;
    document.getElementById("date").innerHTML = date;
}

home = function() {
    console.log("Going home.");
    window.location = "/home";
}

add_project = function() {
    console.log("Adding a project.");
    window.location = "/add_project";
}

my_projects = function() {
    console.log("Navigating to My Projects.");
    window.location = "/my_projects";
}

all_projects = function() {
    console.log("Navigating to All Projects.");
    window.location = "/all_projects";
}

logout = function() {
    console.log("Logging user out.");
    window.location = "/logout";
}
