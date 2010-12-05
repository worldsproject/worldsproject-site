<?php
require_once("template.php"); 

$page = new Page("template.html"); 

$page->replace_tags(array( 
  "description" => "The home of WorldsProject, a place to design and create awesome tools and work.",
  "title" => "Home", 
  "heading" => "Welcome to Worlds Project.", 
  "content" => "Worlds Project is dedicated to creating and breathing life into new and improved open source software and hardware, 
      that anyone is able to use."
)); 

$page->output();
?>
