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


def initialize_db():

    one_month_ago = datetime.now() - timedelta(weeks=4)
    two_month_ago = datetime.now() - timedelta(weeks=8)

    one_week_ago = datetime.now() - timedelta(weeks=1)
    two_week_ago = datetime.now() - timedelta(weeks=2)
    three_week_ago = datetime.now() - timedelta(weeks=3)

    one_day_ago = datetime.now() - timedelta(days=1)
    two_day_ago = datetime.now() - timedelta(days=2)
    three_day_ago = datetime.now() - timedelta(days=3)
    four_day_ago = datetime.now() - timedelta(days=4)
    five_day_ago = datetime.now() - timedelta(days=5)
    six_day_ago = datetime.now() - timedelta(days=6)

    one_minute_ago = datetime.now() - timedelta(minutes=1)
    two_minute_ago = datetime.now() - timedelta(minutes=2)
    five_minute_ago = datetime.now() - timedelta(minutes=5)
    ten_minute_ago = datetime.now() - timedelta(minutes=10)
    fifteen_minute_ago = datetime.now() - timedelta(minutes=15)
    thirty_minute_ago = datetime.now() - timedelta(minutes=30)

    # For buzz
    buzz = User(id=1)
    buzz.put()

    e1 = Event(user=buzz, name="e1", created=one_day_ago)
    e1.put()

    e11 = Event(user=buzz, name="e1", created=one_day_ago)
    e11.put()

    e111 = Event(user=buzz, name="e1", created=one_day_ago)
    e111.put()

    e2 = Event(user=buzz, name="e2", created=one_day_ago)
    e2.put()

    e22 = Event(user=buzz, name="e2", created=one_day_ago)
    e22.put()

    e222 = Event(user=buzz, name="e2", created=one_day_ago)
    e222.put()

    e3 = Event(user=buzz, name="e3", created=two_day_ago)
    e3.put()

    e33 = Event(user=buzz, name="e3", created=two_day_ago)
    e33.put()

    e333 = Event(user=buzz, name="e3", created=two_day_ago)
    e333.put()

    e4 = Event(user=buzz, name="e4", created=two_day_ago)
    e4.put()

    e44 = Event(user=buzz, name="e4", created=two_day_ago)
    e44.put()

    e444 = Event(user=buzz, name="e4", created=two_day_ago)
    e444.put()

    e5 = Event(user=buzz, name="e5", created=three_day_ago)
    e5.put()

    e55 = Event(user=buzz, name="e5", created=three_day_ago)
    e55.put()

    e555 = Event(user=buzz, name="e5", created=three_day_ago)
    e555.put()

    e6 = Event(user=buzz, name="e6", created=three_day_ago)
    e6.put()

    e66 = Event(user=buzz, name="e6", created=three_day_ago)
    e66.put()

    e666 = Event(user=buzz, name="e6", created=three_day_ago)
    e666.put()
