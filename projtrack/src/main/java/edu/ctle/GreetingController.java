package edu.ctle;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
public class GreetingController {

  @RequestMapping(value="/", method=RequestMethod.GET)
  public String greeting(Model model) {
    return "index";
  }

  @RequestMapping("/not_auth")
  public String nope(Model model) {
    return "not_auth";
  }

  @RequestMapping(value="/add_project.html", method=RequestMethod.GET)
  public String add_project(Model model) {
    return "add_project";
  }

  @RequestMapping("/admin.html")
  public String admin_page(Model model) {
    return "admin";
  }

  @RequestMapping("/all_projects.html")
  public String all_projects(Model model) {
    return "all_projects";
  }

  @RequestMapping("/home.html")
  public String home(Model model) {
    return "home";
  }

  @RequestMapping("/my_projects.html")
  public String my_projects(Model model) {
    return "my_projects";
  }

  @RequestMapping("/logout")
  public String logout(Model model) {
    return "logout";
  }

  @RequestMapping("/404.html")
  public String render404(Model model) {
    // Add model attributes
    return "404";
  }
}
