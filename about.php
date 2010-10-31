<?php
require_once("template.php"); 

$page = new Page("template.html"); 

$page->replace_tags(array( 
  "title" => "About", 
  "heading" => "About Worlds Project", 
  "content" => "Worlds Project is a loose conglomaraion of hackers and open source advocates trying to create new things."
)); 

$page->output();
?>
