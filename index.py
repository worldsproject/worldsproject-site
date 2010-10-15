import os

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#Don't forget the page values are: "title", "heading", and "content".
#The current happenings are to be handled by a seperate script.

path = os.path.join(os.path.dirname(__file__), 'index.html')

class MainPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title': "Home",
      'heading': "Welcome to Worlds Project.",      
      'content': """Worlds Project is dedicated to creating and breathing life into new and improved open source software and hardware, 
      that anyone is able to use."""
      }

    
    self.response.out.write(template.render(path, template_values))
    
class AboutPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title': "About",
      'heading': "About Worlds Project",      
      'content': "Worlds Project is a loose conglomaraion of hackers and open source advocates trying to create new things.",
      }
      
    self.response.out.write(template.render(path, template_values))
    
class ProjectPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title': "Our Projects",
      'heading': "Current (and some past) Projects",      
      'content': """<ul class="img_green">
                        <li><h3><a href="/fluxware/index.html">Fluxware</a></h3></li>
                        <p>Fluxware is a Game Engine and Game Development Toolkit, that facilitates the easier creation
                        of new games. Currently the Engine is only available in the Java programming language, however there
                        are plans to migrate to other languages as well, including C#, Python and C++.
                    </ul>""",
      }
      
    self.response.out.write(template.render(path, template_values))
    
class FirehosePage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title': "DIY",
      'heading': "Web Guide for App Engine",      
      'content': "Deploying Static Sites to App Engine",
      }
      
    self.response.out.write(template.render(path, template_values))
    
class ContactPage(webapp.RequestHandler):
  def get(self):

    template_values = {
      'title': "Contact",
      'heading': "How and who to contact",      
      'content': """<b>Just remember, all of our email addresses end with worldsproject.org</b><br />
                  If you're having problems with one of our programs, email us @ help<br />
                  If you want to give us suggestions try emailing @ suggestion<br />
                  For anything else, just email contact<br />
                  Have a good one!""",
      }
      
    self.response.out.write(template.render(path, template_values))
    
application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                     ('/index.html', MainPage),
                                     ('/about.html', AboutPage),
                                     ('/projects.html', ProjectPage),
                                     ('/firehose.html', FirehosePage),
                                     ('/contact.html', ContactPage)],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
