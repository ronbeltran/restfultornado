from google.appengine.ext import db


class User(db.Model):
    id = db.IntegerProperty(required=True)
    username = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class Event(db.Model):
    user = db.ReferenceProperty(User)
    eventname = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


def initialize_db():

    # For buzz
    buzz = User(id=1, username="buzz")
    buzz.put()
    e1 = Event(user=buzz, eventname="e1")
    e1.put()
    e2 = Event(user=buzz, eventname="e2")
    e2.put()
    e3 = Event(user=buzz, eventname="e3")
    e3.put()
    e4 = Event(user=buzz, eventname="e4")
    e4.put()
    e5 = Event(user=buzz, eventname="e5")
    e5.put()

    # For woody
    woody = User(id=2, username="woody")
    woody.put()
    e6 = Event(user=woody, eventname="e6")
    e6.put()
    e7 = Event(user=woody, eventname="e7")
    e7.put()
    e8 = Event(user=woody, eventname="e8")
    e8.put()
    e9 = Event(user=woody, eventname="e9")
    e9.put()
    e10 = Event(user=woody, eventname="e10")
    e10.put()

    # For lenny
    lenny = User(id=3, username="lenny")
    lenny.put()
    e11 = Event(user=lenny, eventname="e11")
    e11.put()
    e12 = Event(user=lenny, eventname="e12")
    e12.put()
    e13 = Event(user=lenny, eventname="e13")
    e13.put()
    e14 = Event(user=lenny, eventname="e14")
    e14.put()
    e15 = Event(user=lenny, eventname="e15")
    e15.put()

    # For squeeze
    squeeze = User(id=4, username="squeeze")
    squeeze.put()
    e16 = Event(user=squeeze, eventname="e16")
    e16.put()
    e17 = Event(user=squeeze, eventname="e17")
    e17.put()
    e18 = Event(user=squeeze, eventname="e18")
    e18.put()
    e19 = Event(user=squeeze, eventname="e19")
    e19.put()
    e20 = Event(user=squeeze, eventname="e20")
    e20.put()

    # For wheezy
    wheezy = User(id=5, username="wheezy")
    wheezy.put()
    e21 = Event(user=wheezy, eventname="e21")
    e21.put()
    e22 = Event(user=wheezy, eventname="e22")
    e22.put()
    e23 = Event(user=wheezy, eventname="e23")
    e23.put()
    e24 = Event(user=wheezy, eventname="e24")
    e24.put()
    e25 = Event(user=wheezy, eventname="e25")
    e25.put()
