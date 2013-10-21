#!/usr/bin/env python

import unittest
import requests


class TestCase(unittest.TestCase):

    def test_app_up(self):
        i = requests.get("http://localhost:8080/")
        assert i.status_code == 200

    def test_events_get(self):
        i = requests.get("http://localhost:8080/api/v1/events")
        assert i.status_code == 403

    def test_events_post(self):
        i = requests.post("http://localhost:8080/api/v1/events/1/event1")
        assert i.status_code == 200


if __name__=="__main__":
    unittest.main()
