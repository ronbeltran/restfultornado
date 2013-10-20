#!/usr/bin/env python

import os
import tornado.web
import tornado.wsgi


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


class EventApiHandler(tornado.web.RequestHandler):

    def get(self):
        raise tornado.web.HTTPError(403)


class EventApiSaveHandler(tornado.web.RequestHandler):

    def post(self, uid, event):
        raise tornado.web.HTTPError(403)


settings = {
    "title": u"Restful Json Api",
    "debug": os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'),
}


application = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
    (r"/api/v1/events", EventApiHandler),
    (r"/api/v1/events/([0-9]+)/(\w+)", EventApiSaveHandler),
], **settings)
