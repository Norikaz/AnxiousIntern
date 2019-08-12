import webapp2
import jinja2
import os
from google.appengine.ext import ndb
from google.appengine.api import users

#jinja env
jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#datastore

class Profile(ndb.Model):
    fullname = ndb.StringProperty(required=True)
    email = ndb.StringProperty()
    resume = ndb.StringProperty(required=False)
    git_link = ndb.StringProperty(required=False)
    Languages = ndb.StringProperty(required=False)
    cov_letter = ndb.StringProperty(required=False)
    hs_trans = ndb.StringProperty(required=False)
    cu_trans = ndb.StringProperty(required=False)
    co_trans = ndb.StringProperty(required=False)


#handlers
class Login(webapp2.RequestHandler):
  def get(self):
    login_template = jinja_env.get_template('templates/login.html')
    saveduser_template = jinja_env.get_template('templates/saved_user.html')
    setup_template = jinja_env.get_template('templates/setup.html')
    user = users.get_current_user()
    sign_out_link = users.create_logout_url('/')
    sign_in_link = users.create_login_url('/')
    # If the user is logged in...
    if user:
        email_address = user.nickname()
        profile_info = Profile.query().filter(Profile.email==email_address).get()
          #If the user has previously been to our site, we greet them!

        if profile_info:
            info_dict={
              "fname":profile_info.fullname,
              "Resume":profile_info.resume,
              "Git":profile_info.git_link,
              "Languages":profile_info.Languages,
              "cover_letter":profile_info.cov_letter,
              "hs_trans":profile_info.hs_trans,
              "cu_trans":profile_info.cu_trans,
              "co_trans":profile_info.co_trans,
              "sign_out": sign_out_link
              }
            self.response.write(saveduser_template.render(info_dict))
              #If the user hasn't been to our site, we ask them to sign up

        else:
            self.response.write(setup_template.render())
                  # Otherwise, the user isn't logged in!

    else:
         signin_dict={
            "signinlink":sign_in_link
         }
         self.response.write(login_template.render(signin_dict))


  def post(self):
        user = users.get_current_user()
        sign_out_link = users.create_logout_url('/')
        email_address = user.nickname()
        su_template = jinja_env.get_template('templates/saved_user.html')
        Fullname = self.request.get('name')
        email =  user.nickname()
        Resume = self.request.get('resume')
        Git = self.request.get('Git')
        Languages = self.request.get('lang')
        cov_letter = self.request.get('cover_letter')
        hs_trans = self.request.get('hs_trans')
        cu_trans = self.request.get('cu_trans')
        co_trans = self.request.get('co_trans')
        acc_profile = Profile(fullname=Fullname,email=email,resume=Resume,git_link=Git,Languages=Languages,cov_letter=cov_letter,hs_trans=hs_trans,cu_trans=cu_trans,co_trans=co_trans)
        acc_profile.put()
        user_info ={
             "fname":acc_profile.fullname,
             "Resume":acc_profile.resume,
             "Git":acc_profile.git_link,
             "Languages":acc_profile.Languages,
             "cover_letter":acc_profile.cov_letter,
             "hs_trans":acc_profile.hs_trans,
             "cu_trans":acc_profile.cu_trans,
             "co_trans":acc_profile.co_trans,
            "sign_out": sign_out_link
        }
        self.response.write(su_template.render(user_info))



class New_Userpage(webapp2.RequestHandler):
    def post(self):
        pass
        # user = users.get_current_user()
        # sign_out_link = users.create_logout_url('/')
        # email_address = user.nickname()
        # user_page_template = jinja_env.get_template('templates/userpage.html')
        # Fullname = self.request.get('name')
        # email =  user.nickname()
        # Resume = self.request.get('resume')
        # Git = self.request.get('Git')
        # Languages = self.request.get('lang')
        # cov_letter = self.request.get('cover_letter')
        # hs_trans = self.request.get('hs_trans')
        # cu_trans = self.request.get('cu_trans')
        # co_trans = self.request.get('co_trans')
        # acc_profile = Profile(fullname=Fullname,email=email,resume=Resume,git_link=Git,Languages=Languages,cov_letter=cov_letter,hs_trans=hs_trans,cu_trans=cu_trans,co_trans=co_trans)
        # acc_profile.put()
        # user_info ={
        #      "fname":acc_profile.fullname,
        #      "Resume":acc_profile.resume,
        #      "Git":acc_profile.git_link,
        #      "Languages":acc_profile.Languages,
        #      "cover_letter":acc_profile.cov_letter,
        #      "hs_trans":acc_profile.hs_trans,
        #      "cu_trans":acc_profile.cu_trans,
        #      "co_trans":acc_profile.co_trans,
        #     "sign_out": sign_out_link
        # }
        # self.response.write(user_page_template.render(user_info))

# class sign_up(webapp2.RequestHandler):
#     def get(self):
#         sign_up_template = jinja_env.get_template('templates/sign_up.html')
#         self.response.write(sign_up_template.render())
#     def post(self):
#         user_page_template = jinja_env.get_template('templates/userpage.html')
#         self.response.write(user_page_template.render())
class Setup(webapp2.RequestHandler):
    def get(self):
        pass
        # setup_template = jinja_env.get_template('templates/setup.html')
        # self.response.write(setup_template.render())
class saveduser(webapp2.RequestHandler):
    def get(self):
        pass
class Essay(webapp2.RequestHandler):
    def get(self):
        essay_template = jinja_env.get_template('templates/essay.html')
        self.response.write(essay_template.render())
class Interveiw(webapp2.RequestHandler):
    def get(self):
        interview_template = jinja_env.get_template('templates/interview.html')
        self.response.write(interview_template.render())
class Update(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        email_address = user.nickname()
        profile_info = Profile.query().filter(Profile.email==email_address).get()
        update_template = jinja_env.get_template('templates/update.html')
        info_dict={
             "fname":profile_info.fullname,
             "Resume":profile_info.resume,
             "Git":profile_info.git_link,
             "Languages":profile_info.Languages,
             "cover_letter":profile_info.cov_letter,
             "hs_trans":profile_info.hs_trans,
             "cu_trans":profile_info.cu_trans,
             "co_trans":profile_info.co_trans,
              }
        self.response.write(update_template.render(info_dict))
    def post(self):
        user = users.get_current_user()
        email_address = user.nickname()
        profile_info = Profile.query().filter(Profile.email==email_address).get()
        sign_out_link = users.create_logout_url('/')
        su_template = jinja_env.get_template('templates/saved_user.html')
        Fullname = self.request.get('name')
        Resume = self.request.get('resume')
        Git = self.request.get('Git')
        Languages = self.request.get('lang')
        cov_letter = self.request.get('cover_letter')
        hs_trans = self.request.get('hs_trans')
        cu_trans = self.request.get('cu_trans')
        co_trans = self.request.get('co_trans')
        profile_info.fullname = Fullname
        profile_info.resume = Resume
        profile_info.git_link = Git
        profile_info.Languages = Languages
        profile_info.cov_letter = cov_letter
        profile_info.hs_trans = hs_trans
        profile_info.cu_trans = cu_trans
        profile_info.co_trans = co_trans
        profile_info.put()
        user_info ={
            "fname":profile_info.fullname,
            "Resume":profile_info.resume,
            "Git":profile_info.git_link,
            "Languages":profile_info.Languages,
            "cover_letter":profile_info.cov_letter,
            "hs_trans":profile_info.hs_trans,
            "cu_trans":profile_info.cu_trans,
            "co_trans":profile_info.co_trans,
            "sign_out": sign_out_link
        }
        self.response.write(su_template.render(user_info))

#routes
app = webapp2.WSGIApplication([
    ('/',Login),
    ('/userspage',New_Userpage),
    ('/setupinfo',Setup),
    ("/saveduser",saveduser),
    ('/essay',Essay),
    ('/interview',Interveiw),
    ('/update',Update)
],debug=True)
