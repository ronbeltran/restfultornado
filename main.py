#!/usr/bin/env python

import logging
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
        self.write("Hello, world")


class EventApiHandler(tornado.web.RequestHandler):

    def get(self):
        raise tornado.web.HTTPError(403)


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
    (r"/api/v1/events", EventApiHandler),
    (r"/api/v1/events/([0-9]+)/([\w]+)", EventApiSaveHandler),
], **settings)
