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
