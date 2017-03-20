load_navbar = function() {
    console.log("Navbar loading.");
    var bar = "<table><th>";
    bar += "<td><button onclick='home()'>Home</button></td>";
    bar += "<td><button onclick='my_projects()'>My Projects</button></td>";
    bar += "<td><button onclick='add_project()'>Add Project</button></td>";
    bar += "<td><button onclick='add_client()'>Add Client</button></td>";
    bar += "<td><button onclick='reports()'>Reports</button></td>";
    bar += "<td><button onclick='all_clients()'>All Clients</button></td>";
    bar += "<td><button onclick='all_projects()'>All Projects</button></td>";
    bar += "<td><button onclick='logout()'>Sign Out</button></td>";
    bar += "</th></table>";
    document.getElementById("navbar").innerHTML = bar;
}

home = function() {
    console.log("Going home.");
    window.location = "/projtrack3/home/";
}

reports = function() {
    console.log("Navigating to Reports.");
    window.location = "/projtrack3/report_page/";
}

add_project = function() {
    console.log("Adding a project.");
    window.location = "/projtrack3/add_project/";
}

my_projects = function() {
    console.log("Navigating to My Projects.");
    window.location = "/projtrack3/my_projects/";
}

all_projects = function() {
    console.log("Navigating to All Projects.");
    window.location = "/projtrack3/all_projects/";
}

add_client = function() {
    console.log("Navigating to Add Client.");
    window.location = "/projtrack3/add_client/";
}

all_clients = function() {
    console.log("Navigating to All Clients.");
    window.location = "/projtrack3/client_view/";
}

logout = function() {
    console.log("Logging user out.");
    window.location = "/projtrack3/logout/";
}
