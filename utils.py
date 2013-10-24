import json
from datetime import datetime, timedelta

def timedelta_wrapper(time, delta=0):
    """ This method is a wrapper for built in method timedelta() 
    since we don't know what the request argument time period.
    Arguments:    
    time is any of the following (hours, days, weeks, months) 
    delta is any value supplied to timedelta() eg. timedelta(hours=3)
    """
    # check if time period is None
    if not time:
        # will return sensible value timedelta(hours=0)
        time = "hours"
    else:
        time = time.lower()

    delta = int(delta)

    if time == "minutes":
        return timedelta(minutes=delta)
    if time == "hours":
        return timedelta(hours=delta)
    elif time == "days":
        return timedelta(days=delta)
    elif time == "weeks":
        return timedelta(weeks=delta)
    else:
        return None


def json_encode(value):
    """JSON-encodes the given Python object.
    Simple workaround to pretty-print json response. Copied from tornado.escape.json_encode
    """
    # JSON permits but does not require forward slashes to be escaped.
    # This is useful when json data is emitted in a <script> tag
    # in HTML, as it prevents </script> tags from prematurely terminating
    # the javscript.  Some json libraries do this escaping by default,
    # although python's standard library does not, so we do it here.
    # http://stackoverflow.com/questions/1580647/json-why-are-forward-slashes-escaped
    return json.dumps(value, sort_keys=True, indent=4).replace("</", "<\\/")


def filter_by(time=None, events_list=[], epoch=None):
    """ Filter event list by minutes, hours, days, months"""
    list_of_list = []
    group_list = []

    increment = 1
    now = datetime.now()

    while epoch <= now:

        if time in ['minutes','hours','days','weeks']:
            group_list = filter(lambda x: x.created >= epoch and x.created <= (epoch + timedelta_wrapper(time, delta=increment)), [e for e in events_list])
            # get the list of event values
            events_name = filter(lambda x: x, [x.to_dict()["name"] for x in group_list])
            for i in set(events_name):
                list_of_list.append(
                    {
                      "date":str(epoch.strftime("%A, %d. %B %Y %I:%M%p")),
                      "event":i, 
                      "count":events_name.count(i)
                    }
                ) 
            epoch += timedelta_wrapper(time, delta=increment) 
            increment += 1

    return list_of_list
