To run tests, setup a virtualenv outside this directory.

    virtualenv test-env
    source test-env/bin/activate
    pip install requests

Change into project directory and run the tests.py.

Application is deployed on http://restfultornado.appspot.com/


    GET   / - Returns list of users
    GET   /api/v1/events/<id> - Returns list of user's events
    POST   /api/v1/events/<id>/<event> - Store event to user identified by user <id>
    GET   /api/v1/events/<id>?time=<time>&delta=<delta> - Returns list of user's events from last X time

where:
- time in ['minutes','hours','days','weeks']
- delta is any int.

Initial data is included in models.py for testing/viewing.
