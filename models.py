from google.appengine.ext import db
from tornado.escape import json_encode


class User(db.Model):
    id = db.IntegerProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    def to_dict(self):
        return dict(id=int(self.id),
                    created=str(self.created.isoformat()))


class Event(db.Model):
    user = db.ReferenceProperty(User, collection_name='user_events')
    name = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    def to_dict(self):
        return dict(user_id=int(self.user.id),
                    name=str(self.name),
                    created=str(self.created.isoformat()))


def initialize_db():

    # For buzz
    buzz = User(id=1)
    buzz.put()

    e1 = Event(user=buzz, name="e1")
    e1.put()

    e2 = Event(user=buzz, name="e2")
    e2.put()

    e3 = Event(user=buzz, name="e3")
    e3.put()

    e4 = Event(user=buzz, name="e4")
    e4.put()

    e5 = Event(user=buzz, name="e5")
    e5.put()

    e6 = Event(user=buzz, name="e5")
    e6.put()

    # For woody
    woody = User(id=2)
    woody.put()

    e6 = Event(user=woody, name="e1")
    e6.put()

    e7 = Event(user=woody, name="e2")
    e7.put()

    e8 = Event(user=woody, name="e3")
    e8.put()

    e9 = Event(user=woody, name="e4")
    e9.put()

    e10 = Event(user=woody, name="e5")
    e10.put()

    # For lenny
    lenny = User(id=3)
    lenny.put()

    e11 = Event(user=lenny, name="e1")
    e11.put()

    e12 = Event(user=lenny, name="e2")
    e12.put()

    e13 = Event(user=lenny, name="e3")
    e13.put()

    e14 = Event(user=lenny, name="e4")
    e14.put()

    e15 = Event(user=lenny, name="e5")
    e15.put()

    # For squeeze
    squeeze = User(id=4)
    squeeze.put()

    e16 = Event(user=squeeze, name="e1")
    e16.put()

    e17 = Event(user=squeeze, name="e2")
    e17.put()

    e18 = Event(user=squeeze, name="e3")
    e18.put()

    e19 = Event(user=squeeze, name="e4")
    e19.put()

    e20 = Event(user=squeeze, name="e5")
    e20.put()

    # For wheezy
    wheezy = User(id=5)
    wheezy.put()

    e21 = Event(user=wheezy, name="e1")
    e21.put()

    e22 = Event(user=wheezy, name="e2")
    e22.put()

    e23 = Event(user=wheezy, name="e3")
    e23.put()

    e24 = Event(user=wheezy, name="e4")
    e24.put()

    e25 = Event(user=wheezy, name="e5")
    e25.put()
