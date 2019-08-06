import webapp2
import jinja2
import os
from server import Accounts

#functions


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
    def post(self):
        user_page_template = jinja_env.get_template('templates/userpage.html')
        username = self.request.get('username')
        password = self.request.get('password')
        login_info = Accounts(db_username=username,db_password=password)
        all_accs = Accounts.query().fetch()
        key = all_accs.query(all_accs.db_username == login_info.db_username).fetch()
        user_dict={
            "name":full_name
        }
        self.response.write(user_page_template.render(user_dict))

class sign_up(webapp2.RequestHandler):
    def get(self):
        sign_up_template = jinja_env.get_template('templates/sign_up.html')
        self.response.write(sign_up_template.render())
    def post(self):
        user_page_template = jinja_env.get_template('templates/userpage.html')
        name = self.request.get('name')
        new_account_username = self.request.get('new_user')
        new_account_password = self.request.get('new_user_password')
        new_accounts = Accounts(db_username=new_account_username,db_password=new_account_password)
        acc_id = new_accounts.put()
        user_info = Profile(db_name=name, owner=acc_id)
        user_info.put()
        acc_info ={
            "username":new_account_username,
            "password":new_account_password,
            "name": name
        }
        self.response.write(user_page_template.render(acc_info))



#routes
app = webapp2.WSGIApplication([
    ('/',Login),
    ('/userspage',Userpage),
    ('/sign_up',sign_up)
],debug=True)
