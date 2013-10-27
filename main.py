#!/usr/bin/env python

import os
import random
import time as timer

from datetime import datetime, timedelta

import tornado.web
import tornado.wsgi

from google.appengine.ext import db

import models
import utils

# initialize users and events 
if models.User.all().count() == 0:
    models.initialize_db()

MAX_NUMBER_OF_EVENTS = 500


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        """ Show list of users
        """
        start = timer.time()
        data = {
            "users": [u.to_dict() for u in models.User.all()],
            "load_time": timer.time() - start
        }
        self.write(utils.json_encode(data))


class EventApiHandler(tornado.web.RequestHandler):

    def get(self, user_id):
        """
        Return the number of events of a user.

        :Arguments:
            user_id : int
                User id
            time : str
                Time represents ``minutes``, ``days``, ``hours``, ``weeks`` in datetime.timedelta() eg. datetime.timedelta(days=7)
            delta : int
                Delta is any int value for datetime.timedelta() eg. datetime.timedelta(days=7)

        If no valid time query argument is provided, it will show the user events count. 
        """

        start = timer.time()
        user = models.User.all().filter("id =",int(user_id)).get()

        if not user:
            raise tornado.web.HTTPError(404)

        time = self.get_argument("time", None)
        delta = self.get_argument("delta", 0)

        # get last x hours, days, weeks, months
        last_x_time = datetime.now() - utils.timedelta_wrapper(time, int(delta))

        # get events from the last x time
        events_from_last_x_time = filter(lambda x: x.created >= last_x_time, [event for event in user.user_events] )

        data = {}

        if not time:
            # show all events for user
            data["description"] = "Number of events for User %s" % (str(user_id))
            data["load_time"] = timer.time() - start
            data["events"] = user.user_events.count()
        else:
            data["description"] = "Number of events for User %s for the last %s %s" % (str(user_id), str(delta), str(time))
            data["load_time"] = timer.time() - start
            data["grouping"] = utils.filter_by(time, events_from_last_x_time, last_x_time)

        self.write(utils.json_encode(data))


class EventApiSaveHandler(tornado.web.RequestHandler):

    def post(self, user_id, eventname):
        """
        Store the event and associate it to a user identified by user_id

        :Arguments:
            user_id : int
                User id
            event_name : str
                Any string representing an event 
        """

        existing = models.User.all().filter("id =", int(user_id)).get()
        if not existing:
            raise tornado.web.HTTPError(400)
        else:
            event = models.Event(user=existing, name=eventname)
            event.put()
            self.set_status(201)


class GenerateRandomEventsHandler(tornado.web.RequestHandler):

    def get(self):
        """Batch delete."""

        start = timer.time()
        count = int( models.Event.all().count() );

        # check if there is something to delete
        if count > 0:
            db.delete([item for item in models.Event.all()])

        if models.Event.all().count() == 0:
            self.write( utils.json_encode({
                                          'message':'All events succesfully deleted.',
                                          'load_time': timer.time() - start
                                          }) )
        else:
            self.write( utils.json_encode({
                                          'message':'Delete failed. Try again.',
                                          'load_time': timer.time() - start
                                          }) )


    def post(self):
        """ 
        Generate randmomized events for a user.

        :Arguments:
            user_id : int
                User id
            num_of_events : int
                Number of events to generate, max of 100,000 per request
            time : str
                Time represents ``minutes``, ``days``, ``hours``, ``weeks`` in datetime.timedelta() eg. datetime.timedelta(days=7)
            delta : int
                Delta is any int value for datetime.timedelta() eg. datetime.timedelta(days=7)
        """ 
        start = timer.time()
        time = self.get_argument("time", None)
        delta = self.get_argument("delta", 0)
        num_of_events = self.get_argument("num_of_events", 0)
        user_id = self.get_argument("user_id", 0)

        time = str(time) if time in ['minutes','hours','days','weeks'] else None

        if not time:
            raise tornado.web.HTTPError(404)

        user = models.User.all().filter("id =",int(user_id)).get()

        if not user:
            raise tornado.web.HTTPError(404)


        if int(num_of_events) > MAX_NUMBER_OF_EVENTS:
            num_of_events = MAX_NUMBER_OF_EVENTS 

        now = datetime.now()

        for i in xrange(1,int(num_of_events)+1):
            r = random.randrange(1,int(delta))
            e = models.Event(user=user, 
                             name='Event'+str(r), 
                             created=now - utils.timedelta_wrapper(time, int(r)) )
            e.put()

        d = {}
        d["load_time"] = timer.time() - start 
        d["count"] = models.Event.all().count() 

        return self.write(utils.json_encode(d))


settings = {
    "title": u"Restful Json Api",
    "debug": os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'),
}


application = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
    (r"/api/v1/events/randomize", GenerateRandomEventsHandler),
    (r"/api/v1/events/([0-9]+)", EventApiHandler),
    (r"/api/v1/events/([0-9]+)/([\w]+)", EventApiSaveHandler),
], **settings)
