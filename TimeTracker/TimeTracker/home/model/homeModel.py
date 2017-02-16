from google.appengine.ext import ndb

class AccountModel(ndb.Model):
    first_name = ndb.StringProperty(indexed=True, required=True)
    last_name = ndb.StringProperty(indexed=True, required=True)
    user_id = ndb.StringProperty(indexed=True, required=True)

