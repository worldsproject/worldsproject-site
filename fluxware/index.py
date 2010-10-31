import os
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#Don't forget the page values are: "title", "heading", and "content".
#The current happenings are to be handled by a seperate script.
#http://twitter.com/statuses/friends_timeline/204267049.rss
path = os.path.join(os.path.dirname(__file__), 'index.html')

class MainPage(webapp.RequestHandler):
    def get(self):

        template_values = {
          'title': "Home",
          'heading': "Fluxware, making games easy.",      
          'content': """Fluxware is a software package, consisting of a Game Engine, Level Editor, Sp
          rite Editor and Network connectivity software. Our goal is to let anyone have the ability to
          create free and <i>fun</i> games without the need for massive amounts of programming and artistic skill. 
          <br />
          Fluxware focuses on using free, open source technolgy, which enambles you to make any game you want,  your way, with no restrictions. Have fun, be creative, and make a game that you and your friends can all play."""
          }

    
        self.response.out.write(template.render(path, template_values))
    
class AboutPage(webapp.RequestHandler):
    def get(self):

        template_values = {
          'title': "About",
          'heading': """What is this "Fluxware" thing?""",      
          'content': """ <p>Fluxware consists of several different software tools designed to make creation of games simplier and easier then ever before. Let's go through each of the tools, and how they can help you.</p>
          
          <h3>Fluxware Game Engine</h3>
          <p>The Fluxware game engine is the core of Fluxware. A game engine is the toolbox of game creation. It takes care of the small details that you don't want to deal with when creating a game. When you, or someone else, creates a game, you don't want to have to worry about the different keyboards, mice, monitors and hardware that the play <i>could</i> be using. A game engine handles that detail, letting you simply say "I want the character to more <b>here</b>, and letting it come to reality.</p>
          
          <h3>Fluxware Level Editor: Edit</h3>
          <p>The Fluxware Level Editor is designed to make game level creation easier then ever. With a simple drag and drop interface, level saving in both Fluxware and Tiled map formats, you get easy simple compatibility, and easy to edit, <i>readable</i> level files. The Fluxware Level format is so easy to read and type, you <b> don't even need to be a programmer</b> to create fun, exciting and attractive game levels.</p>
          
          <h3>Fluxware Sprite Editor: Forge</h3>
          <p>The Fluxware Sprite Editor is designed to make character creation as simple as possible. With simple image importing and adding actions through a menu based, this flowchart based sprite editor will allow you to create simple to complex sprites, all with a few clicks of the mouse.</p>
          
          <h3>Fluxware Network Connection: Connect</h3>
          <p>Fluxware Network COnnection allows a game creator to setup simple  P2P network software, complete with lobbies, and lobby chat. All it takes is 5 minutes, and you can have your own server online, to play with people all over the world!</p>""",
          }
      
        self.response.out.write(template.render(path, template_values))
    
class MemberPage(webapp.RequestHandler):
    def get(self):

        template_values = {
          'title': "Members",
          'heading': "Current Members",      
          'content': """<img src="http://www.worldsproject.org/tim.jpg" alt="Tim Butram" />
          <p>Tim is one of the original founders of Fluxware, and continues to work on programming on it today.</p>""",
          }
      
        self.response.out.write(template.render(path, template_values))
    
class GamePage(webapp.RequestHandler):
    def get(self):
    
        template_values = {
          'title': "Fluxware Games",
          'heading': "Games made under the Fluxware banner.",      
          'content': """<h3>The Road to Europa</h3>

<p>Fluxware's first attempt at a game.  Includes high flying space shooting action!</p>
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
</p>""",
          }
          
        self.response.out.write(template.render(path, template_values))
    
application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                     ('/index.html', MainPage),
                                     ('/about.html', AboutPage),
                                     ('/members.html', MemberPage),
                                     ('/games.html', GamePage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
