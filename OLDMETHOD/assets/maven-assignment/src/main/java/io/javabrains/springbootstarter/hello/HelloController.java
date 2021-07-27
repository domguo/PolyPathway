package io.javabrains.springbootstarter.hello;

@RestController
public class HelloController {
	
	@RequestMapping("/hello")
	public String sayHi() {
		return"Hello World";
	}
}
