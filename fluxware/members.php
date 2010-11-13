<?php
require_once("../template.php"); 

$page = new Page("template.html"); 

$page->replace_tags(array( 
  "title" => "Members", 
  "heading" => "Who works on Fluxware?", 
  "content" => '<img src="http://www.worldsproject.org/tim.jpg" alt="Tim Butram" />
          <p>Tim is one of the original founders of Fluxware, and continues to work on programming on it today.</p>'
)); 

$page->output();
