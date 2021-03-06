#!/usr/bin/env python

import unittest
import requests


class TestCase(unittest.TestCase):

    def test_app_up(self):
        i = requests.get("http://localhost:8080/")
        assert i.status_code == 200

    def test_events_get(self):
        i = requests.get("http://localhost:8080/api/v1/events/1")
        assert i.status_code == 200

    def test_events_get_not_found(self):
        i = requests.get("http://localhost:8080/api/v1/events/100")
        assert i.status_code == 404

    def test_events_post(self):
        i = requests.post("http://localhost:8080/api/v1/events/1/event1")
        assert i.status_code == 201

    def test_events_post_bad_request(self):
        i = requests.post("http://localhost:8080/api/v1/events/100/event2")
        assert i.status_code == 400

    def test_events_randomize(self):
        data={'user_id':1, 'num_of_events':100, 'time':'days', 'delta':7}
        i = requests.post("http://localhost:8080/api/v1/events/randomize?user_id=1&num_of_events=5000&time=days&delta=7", params=data)
        assert i.status_code == 200


if __name__=="__main__":
    unittest.main()
