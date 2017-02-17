from google.appengine.ext import ndb

class AccountModel(ndb.Model):
    first_name = ndb.StringProperty()
    last_name = ndb.StringProperty()
    user_id = ndb.StringProperty()

