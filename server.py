from google.appengine.ext import ndb

class Accounts(ndb.Model):
    db_username = ndb.StringProperty(required = True)
    db_password = ndb.StringProperty(required = True)

class Profiles(ndb.Model):
    db_name = ndb.StringProperty(required = True)
    owner = ndb.KeyProperty(Accounts)
