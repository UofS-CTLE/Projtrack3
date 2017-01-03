package hello;

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

    @RequestMapping("/error")
    public String error(Model model) {
      return "404";
    }

}
