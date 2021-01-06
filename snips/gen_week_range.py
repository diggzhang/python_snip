import datetime as dt
import time
import json


def gen_week_range():
    weekend_index = (6, 5)  # Sunday, Saturday
    requested_range = (dt.datetime(2019, 4, 14, 0, 0), dt.datetime(2021, 1, 1, 0, 0))

    start, end = requested_range
    sun, sat = weekend_index
    cur = start
    my_range = []

    while cur < end:
            cr = []
            cr.append(cur)
            cur = end if end < cur+dt.timedelta(days=6) else (cur+dt.timedelta(days=(sun if cur.weekday() == sun else (sat-cur.weekday()))))
            cr.append(cur)
            cur += dt.timedelta(days=1)
            my_range.append(cr)
    return my_range

date_list = gen_week_range()
