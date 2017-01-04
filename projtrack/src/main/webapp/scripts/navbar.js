window.onload = function() {

  var version = "0.1.0";

  console.log("Navbar loading.");
  var bar = "<table><th>";
  bar += "<td><button src='home()'>Home</button></td>";
  bar += "<td><button src='add_project()'>My Projects</button></td>";
  bar += "<td><button src='my_projects()'>Add Project</button></td>";
  bar += "<td><button src='all_projects()'>All Projects</button></td>";
  bar += "</th></table>";
  document.getElementById("navbar").innerHTML = bar;
  document.getElementById("version").innerHTML = version;
}

home = function() {
  window.location = "home.html";
}

add_project = function() {
  window.location = "add_project.html";
}

my_projects = function() {
  window.location = "my_projects.html";
}

all_projects = function() {
  window.location = "all_projects.html";
}
