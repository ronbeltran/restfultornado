#!/usr/bin/env python

import os
import tornado.web
import tornado.wsgi


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


settings = {
    "title": u"Restful Json Api",
    "debug": os.environ.get('SERVER_SOFTWARE', '').startswith('Dev'),
}


application = tornado.wsgi.WSGIApplication([
    (r"/", MainHandler),
], **settings)
