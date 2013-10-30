from datetime import datetime, timedelta
from google.appengine.ext import db


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


class EventCount(db.Model):
    user = db.ReferenceProperty(User, collection_name='user_event_count')
    name = db.StringProperty(required=True)
    count = db.IntegerProperty(default=0)

    def to_dict(self):
        return dict(user_id=int(self.user.id),
                    name=str(self.name),
                    count=str(self.count()))


def initialize_db():

    one_day_ago = datetime.now() - timedelta(days=1)
    two_day_ago = datetime.now() - timedelta(days=2)
    three_day_ago = datetime.now() - timedelta(days=3)
    four_day_ago = datetime.now() - timedelta(days=4)
    five_day_ago = datetime.now() - timedelta(days=5)
    six_day_ago = datetime.now() - timedelta(days=6)

    one_hour_ago = datetime.now() - timedelta(minutes=1)
    two_hour_ago = datetime.now() - timedelta(minutes=2)
    five_hour_ago = datetime.now() - timedelta(minutes=5)
    ten_hour_ago = datetime.now() - timedelta(minutes=10)
    fifteen_hour_ago = datetime.now() - timedelta(minutes=15)
    thirty_hour_ago = datetime.now() - timedelta(minutes=30)

    # For buzz
    buzz = User(id=1)
    buzz.put()

    e1 = Event(user=buzz, name="e1", created=one_hour_ago)
    e1.put()

    e11 = Event(user=buzz, name="e1", created=one_hour_ago)
    e11.put()

    e111 = Event(user=buzz, name="e1", created=one_hour_ago)
    e111.put()

    # ('e1', '1'), ('e1','1'),('e1','1') => ('e1',['1','1','1'])

    e2 = Event(user=buzz, name="e2", created=one_hour_ago)
    e2.put()

    e22 = Event(user=buzz, name="e2", created=two_hour_ago)
    e22.put()

    e222 = Event(user=buzz, name="e2", created=two_hour_ago)
    e222.put()

    # ('e2', '1'), ('e2','2'),('e2','2') => ('e2',['1','2','2'])

    e3 = Event(user=buzz, name="e3", created=five_hour_ago)
    e3.put()

    e33 = Event(user=buzz, name="e3", created=five_hour_ago)
    e33.put()

    e333 = Event(user=buzz, name="e3", created=five_hour_ago)
    e333.put()

    # ('e3', '5'), ('e3','5'),('e3','5') => ('e3',['5','5','5'])

    e4 = Event(user=buzz, name="e4", created=ten_hour_ago)
    e4.put()

    e44 = Event(user=buzz, name="e4", created=ten_hour_ago)
    e44.put()

    e444 = Event(user=buzz, name="e4", created=ten_hour_ago)
    e444.put()

    # ('e4', '10'), ('e4','10'),('e4','10') => ('e4',['10','10','10'])

    e5 = Event(user=buzz, name="e5", created=two_hour_ago)
    e5.put()

    e55 = Event(user=buzz, name="e5", created=two_hour_ago)
    e55.put()

    e555 = Event(user=buzz, name="e5", created=two_hour_ago)
    e555.put()

    # ('e5', '2'), ('e5','2'),('e5','2') => ('e5',['5','5','5'])

    e6 = Event(user=buzz, name="e6", created=two_hour_ago)
    e6.put()

    e66 = Event(user=buzz, name="e6", created=three_hour_ago)
    e66.put()

    e666 = Event(user=buzz, name="e6", created=three_hour_ago)
    e666.put()

    # ('e6', '2'), ('e6','3'),('e6','3') => ('e6',['2','3','3'])

    # For woody 
    woody = User(id=2)
    woody.put()

    e10 = Event(user=woody, name="e1", created=one_hour_ago)
    e10.put()

    e100 = Event(user=woody, name="e1", created=one_hour_ago)
    e100.put()

    e1000 = Event(user=woody, name="e2", created=two_hour_ago)
    e1000.put()
