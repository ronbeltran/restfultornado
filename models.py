from google.appengine.ext import db


class User(db.Model):
    id = db.IntegerProperty(required=True)
    username = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class Event(db.Model):
    user_id = db.ReferenceProperty(User)
    eventname = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


def create_users():

    buzz = User(id=1, username="buzz")
    buzz.put()

    woody = User(id=2, username="woody")
    woody.put()

    lenny = User(id=3, username="lenny")
    lenny.put()

    squeeze = User(id=4, username="squeeze")
    squeeze.put()

    wheezy = User(id=5, username="wheezy")
    wheezy.put()
