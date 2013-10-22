#!/usr/bin/env python

import os
import tornado.web
import tornado.wsgi

from google.appengine.ext import db

import models

# initialize users and events 
if db.Query(models.User).count() == 0:
    models.initialize_db()


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        data = {
            "users": [u.to_dict() for u in models.User.all()],
            "events": [v.to_dict() for v in models.Event.all()],
        }
        self.write(tornado.escape.json_encode(data))


class EventApiHandler(tornado.web.RequestHandler):

    def get(self, user_id):
        data = {}
        user = models.User.all().filter("id =",int(user_id)).get()
        if not user:
            raise tornado.web.HTTPError(404)

        data["user_id"] = int(user.id)
        data["event"] = user.event_set.count()
        self.write(tornado.escape.json_encode(data))


class EventApiSaveHandler(tornado.web.RequestHandler):

    def post(self, user_id, eventname):
        existing = db.Query(models.User).filter("id =", int(user_id)).get()
        if not existing:
            raise tornado.web.HTTPError(404)
        else:
            event = models.Event(user=existing, eventname=eventname)
            event.put()


settings = {
    "title": u"Restful Json Api",
    "debug": os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'),
}


application = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
    (r"/api/v1/events/([0-9]+)", EventApiHandler),
    (r"/api/v1/events/([0-9]+)/([\w]+)", EventApiSaveHandler),
], **settings)
