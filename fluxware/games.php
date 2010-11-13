<?php
require_once("../template.php");  

$page = new Page("template.html"); 

$page->replace_tags(array( 
  "title" => "Games", 
  "heading" => "Games created with Fluxware", 
  "content" => '<h3>The Road to Europa</h3>

<p>Fluxware\'s first attempt at a game.  Includes high flying space shooting action!</p>
<p>
	<a href="./games/roadtoeuropa/images/intro_screen.png">
		<img src="./games/roadtoeuropa/images/thumbnails/intro_screen_thumb.png" alt="Intro Screen">
	</a>
	
	<a href="./games/roadtoeuropa/images/action_shot1.png">
		<img src="./games/roadtoeuropa/images/thumbnails/action_shot1_thumb.png" alt="Action Shot" />
	</a>
	
	<br />
	
	<a href="./games/roadtoeuropa/images/action_shot2.png">
		<img src="./games/roadtoeuropa/images/thumbnails/action_shot2_thumb.png" alt="Action Shot" />
	</a>
	
	<a href="./games/roadtoeuropa/images/boss.png">
		<img src="./games/roadtoeuropa/images/thumbnails/boss_thumb.png" alt="Boss Battle" />
	</a>

	<br />
	
	<a href="./games/roadtoeuropa/more.php">More art and screenshots</a> | <a href="./games/roadtoeuropa/roadtoeuropa.jar">Download Game (15Mb)</a>
</p>'
)); 

$page->output();
