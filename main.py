import webapp2
import jinja2
import os

#jinja env
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


#handlers
class Login(webapp2.RequestHandler):
    def get(self):
        login_template = jinja_env.get_template('templates/login.html')
        self.response.write(login_template.render())


class Userpage(webapp2.RequestHandler):
    def get(self):
        user_page_template = jinja_env.get_template('templates/userpage.html')
        self.response.write(user_page_template.render())

class sign_up(webapp2.RequestHandler):
    def get(self):
        sign_up_template = jinja_env.get_template('templates/sign_up.html')
        self.response.write(sign_up_template.render())
    def post(self):
        user_page_template = jinja_env.get_template('templates/userpage.html')
        self.response.write(user_page_template.render())
class Setup(webapp2.RequestHandler):
    def get(self):
        setup_template = jinja_env.get_template('templates/setup.html')
        self.response.write(setup_template.render())
        pass
#routes
app = webapp2.WSGIApplication([
    ('/',Login),
    ('/userspage',Userpage),
    ('/sign_up',sign_up),
    ('/setupinfo',Setup)
],debug=True)
