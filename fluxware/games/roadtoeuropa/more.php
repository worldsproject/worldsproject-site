<?php
require_once("../../../template.php"); 

$page = new Page("../../template.html"); 

$page->replace_tags(array( 
  "title" => 'The Road to Europa', 
  "heading" => "The Fluxware organizations first game.", 
  "content" => "more.dat"
)); 

$page->output();
?>
