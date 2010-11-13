<?php
require_once("../template.php");  

$page = new Page("template.html"); 

$page->replace_tags(array( 
  "title" => "About", 
  "heading" => "What is this Fluxware thing?", 
  "content" => "<p>Fluxware consists of several different software tools designed to make creation of games simplier and easier then ever before. Let's go through each of the tools, and how they can help you.</p>
          
          <h3>Fluxware Game Engine</h3>
          <p>The Fluxware game engine is the core of Fluxware. A game engine is the toolbox of game creation. It takes care of the small details that you don't want to deal with when creating a game. When you, or someone else, creates a game, you don't want to have to worry about the different keyboards, mice, monitors and hardware that the play <i>could</i> be using. A game engine handles that detail, letting you simply say \"I want the character to more <b>here</b>\", and letting it come to reality.</p>
          
          <h3>Fluxware Level Editor: Edit</h3>
          <p>The Fluxware Level Editor is designed to make game level creation easier then ever. With a simple drag and drop interface, level saving in both Fluxware and Tiled map formats, you get easy simple compatibility, and easy to edit, <i>readable</i> level files. The Fluxware Level format is so easy to read and type, you <b> don't even need to be a programmer</b> to create fun, exciting and attractive game levels.</p>
          
          <h3>Fluxware Sprite Editor: Forge</h3>
          <p>The Fluxware Sprite Editor is designed to make character creation as simple as possible. With simple image importing and adding actions through a menu based, this flowchart based sprite editor will allow you to create simple to complex sprites, all with a few clicks of the mouse.</p>
          
          <h3>Fluxware Network Connection: Connect</h3>
          <p>Fluxware Network COnnection allows a game creator to setup simple  P2P network software, complete with lobbies, and lobby chat. All it takes is 5 minutes, and you can have your own server online, to play with people all over the world!</p>"
)); 

$page->output();
