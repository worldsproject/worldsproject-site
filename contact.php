<?php
require_once("template.php"); 

$page = new Page("template.html"); 

$page->replace_tags(array( 
  "description" => "How to contact WorldsProject.",
  "title" => "Contact", 
  "heading" => "How and who to contact", 
  "content" => "<b>Just remember, all of our email addresses end with worldsproject.org</b><br />
                  If you're having problems with one of our programs, email us @ help<br />
                  If you want to give us suggestions try emailing @ suggestion<br />
                  For anything else, just email contact<br />
                  Have a good one!"
)); 

$page->output();
?>
