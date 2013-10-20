#!/usr/bin/env python

import unittest
import requests


class TestCase(unittest.TestCase):

    def test_app_up(self):
        i = requests.get("http://localhost:8080/")
        assert i.status_code == 200


if __name__=="__main__":
    unittest.main()
