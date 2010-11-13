<?php
require_once("../template.php"); 

$page = new Page("template.html"); 

$page->replace_tags(array( 
  "title" => "Welcome", 
  "heading" => "Game creation made easy.", 
  "content" => 'Fluxware is a software package, consisting of a Game Engine, Level Editor, Sp
          rite Editor and Network connectivity software. Our goal is to let anyone have the ability to
          create free and <i>fun</i> games without the need for massive amounts of programming and artistic skill. 
          <br />
          Fluxware focuses on using free, open source technolgy, which enambles you to make any game you want,  your way, with no restrictions. Have fun, be creative, and make a game that you and your friends can all play.'
)); 

$page->output();
