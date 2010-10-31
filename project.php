<?php
require_once("template.php"); 

$page = new Page("template.html"); 

$page->replace_tags(array( 
  "title" => "Our Projects", 
  "heading" => "Current (and some past) Projects", 
  "content" => '<ul class="img_green">
                        <li><h3><a href="/fluxware/index.html">Fluxware</a></h3></li>
                        <p>Fluxware is a Game Engine and Game Development Toolkit, that facilitates the easier creation
                        of new games. Currently the Engine is only available in the Java programming language, however there
                        are plans to migrate to other languages as well, including C#, Python and C++.
                    </ul>'
)); 

$page->output();
?>
