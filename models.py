from google.appengine.ext import db


class User(db.Model):
    id = db.IntegerProperty(required=True)
    username = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class Event(db.Model):
    user_id = db.ReferenceProperty(User)
    eventname = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
