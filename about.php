<?php
require_once("template.php"); 

$page = new Page("template.html"); 

$page->replace_tags(array(
  "description" => "What WorldsProject is all about.", 
  "title" => "About", 
  "heading" => "About Worlds Project", 
  "content" => "about.dat"
)); 

$page->output();
?>
