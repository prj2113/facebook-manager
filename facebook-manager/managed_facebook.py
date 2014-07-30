import os
import urllib
import jinja2
import webapp2
import sys
sys.path.insert(0,'lib')

import facebook

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

FACEBOOK_APP_ID = "your facebook app id"
FACEBOOK_APP_SECRET ="your facebook app secret"


class MainPage(webapp2.RequestHandler):

	def get(self):
		template = JINJA_ENVIRONMENT.get_template('login.html')
		self.response.write(template.render())


class Photos(webapp2.RequestHandler):

	def get(self):
		token = self.request.cookies.get("token")
		graph = facebook.GraphAPI(token)
		profile = graph.get_object("me")
		news_feed = graph.get_connections("me", "home")
			
		template_values = {
			'name': profile["name"],
			'data': news_feed["data"],
			'userid': profile["id"]
		}
		
		template = JINJA_ENVIRONMENT.get_template('photos.html')
		self.response.write(template.render(template_values))

class SharedLinks(webapp2.RequestHandler):

	def get(self):
		token = self.request.cookies.get("token")
		graph = facebook.GraphAPI(token)
		profile = graph.get_object("me")
		news_feed = graph.get_connections("me", "home")
			
		template_values = {
			'name': profile["name"],
			'data': news_feed["data"],
			'userid': profile["id"]
		}
		
		template = JINJA_ENVIRONMENT.get_template('sharedLinks.html')
		self.response.write(template.render(template_values))


class CheckIn(webapp2.RequestHandler):

	def get(self):
		token = self.request.cookies.get("token")
		graph = facebook.GraphAPI(token)
		profile = graph.get_object("me")
		news_feed = graph.get_connections("me", "home")
			
		template_values = {
			'name': profile["name"],
			'data': news_feed["data"],
			'userid': profile["id"]
		}
		
		template = JINJA_ENVIRONMENT.get_template('checkIn.html')
		self.response.write(template.render(template_values))

class Logout(webapp2.RequestHandler):

	def get(self):
		self.response.delete_cookie("token")
		template = JINJA_ENVIRONMENT.get_template('logout.html')
		self.response.write(template.render())

class Status_page(webapp2.RequestHandler):

	def get(self):
		alert =self.request.cookies.get("token")
		if alert:
			token = alert
		else:	
			token = self.request.GET.get('code')
			self.response.set_cookie('token', token)

		graph = facebook.GraphAPI(token)
		profile = graph.get_object("me")
		news_feed = graph.get_connections("me", "home")
			
		template_values = {
			'name': profile["name"],
			'data': news_feed["data"],
			'userid': profile["id"],
		}
		
		template = JINJA_ENVIRONMENT.get_template('status.html')
		self.response.write(template.render(template_values))




application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/status.html/',Status_page),
   	('/photos.html/',Photos),
   	('/sharedLinks.html/',SharedLinks),
   	('/checkIn.html/',CheckIn),
   	('/logout.html/',Logout)

], debug=True)