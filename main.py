#!/usr/bin/env python

import os
from datetime import datetime, timedelta

import tornado.web
import tornado.wsgi

from google.appengine.ext import db

import models
import utils

# initialize users and events 
if models.User.all().count() == 0:
    models.initialize_db()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        """ Show list of users
        """
        data = {
            "users": [u.to_dict() for u in models.User.all()],
        }
        self.write(utils.json_encode(data))


class EventApiHandler(tornado.web.RequestHandler):

    def get(self, user_id):
        """
        Return the number of events of a user per below requirements:
        - Per Hour
        - Per Day 
        - Per 7 Days or 1 Week 
        - Per Per Month
        """

        user = models.User.all().filter("id =",int(user_id)).get()

        if not user:
            raise tornado.web.HTTPError(404)

        time = self.get_argument("time", None)
        delta = self.get_argument("delta", 0)

        # get last x hours, days, weeks, months
        last_x_time = utils.timedelta_wrapper(time, int(delta))

        # get events from the last x time
        events_from_last_x_time = filter(lambda x: x.created >= last_x_time, [event for event in user.user_events] )

        count_list = []
        data = {}
        data["description"] = "All Events for User %s for the last %s %s" % (str(user_id), str(delta), str(time))

        for i in events_from_last_x_time:
            item = {
                "Event":i.name,
                "Count":"",
                "Created":i.created.strftime("%b %d %Y %I:%M%p %Z"),
            }
            count_list.append(item)

        if not time:
            # show all events for user
            data["events"] = [u.to_dict() for u in user.user_events]
        else:
            data["grouping"] = utils.filter_by(time, events_from_last_x_time, last_x_time)

        self.write(utils.json_encode(data))


class EventApiSaveHandler(tornado.web.RequestHandler):

    def post(self, user_id, eventname):
        existing = models.User.all().filter("id =", int(user_id)).get()
        if not existing:
            raise tornado.web.HTTPError(400)
        else:
            event = models.Event(user=existing, name=eventname)
            event.put()
            self.set_status(201)


settings = {
    "title": u"Restful Json Api",
    "debug": os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'),
}


application = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
    (r"/api/v1/events/([0-9]+)", EventApiHandler),
    (r"/api/v1/events/([0-9]+)/([\w]+)", EventApiSaveHandler),
], **settings)
