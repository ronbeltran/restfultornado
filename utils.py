import json
from datetime import datetime, timedelta

def timedelta_wrapper(time, delta=0):
    """ This method is a wrapper for built in method timedelta() 
    since we don't know what the request argument time period.
    Arguments:    
    time is any of the following (hours, days, weeks, months) 
    delta is any value supplied to timedelta() eg. timedelta(hours=3)
    """
    now = datetime.now() 
    # check if time period is None
    if not time:
        # will return sensible value timedelta(hours=0)
        time = "hours"
    else:
        time = time.lower()

    ret_val = None
    delta = int(delta)

    if time == "minutes":
        ret_val = now - timedelta(minutes=delta)
    if time == "hours":
        ret_val = now - timedelta(hours=delta)
    elif time == "days":
        ret_val = now - timedelta(days=delta)
    elif time == "weeks":
        ret_val = now - timedelta(weeks=delta)
    elif time == "months":
        ret_val = now - timedelta(months=delta)
    else:
        pass
    return ret_val


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
    between = None 

    while epoch <= datetime.now():

        if time == 'days':
            group_list = filter(lambda x: x.created >= epoch and x.created <= (epoch + timedelta(days=increment)), [e for e in events_list])
            list_of_list.append(
                [d.to_dict() for d in group_list]
            ) 
            epoch += timedelta(days=increment) 
            increment+=1

    return list_of_list
