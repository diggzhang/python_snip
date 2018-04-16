import datetime

start = datetime.datetime.strptime("21-06-2017", "%d-%m-%Y")
end = datetime.datetime.strptime("07-07-2017", "%d-%m-%Y")

start = datetime.datetime(2016, 9, 11, 16)
end = datetime.datetime(2017, 1, 22, 16)


def echo_split_line_by_lrjust(split_string, direction, iter_range, symbol):
    direction_map = {
        0: "c",
        1: "l",
        2: "r"
    }
    return_string = {
        "l": split_string.ljust(iter_range, symbol),
        "r": split_string.rjust(iter_range, symbol),
        "c": split_string.center(iter_range, symbol)
    }
    return return_string.get(direction_map.get(direction))


def dump_json_gen(time_range):
    # ISODate("2016-09-13T16:24:31.010Z")
    start_date = time_range["start"].strftime("%Y-%m-%dT%H:00:00.000Z")
    end_date = time_range["end"].strftime("%Y-%m-%dT%H:00:00.000Z")
    return """
        {
            "serverTime": {
                "$gte": ISODate("%s"),
                "$lt": ISODate("%s")
            },
            "platform": "backend"
        }
    """%(start_date, end_date)


def time_range_gen(start, end):
    time_range = []
    while start < end:
        this_date_range_dict = {}
        this_date_range_dict["start"] = start
        start = start + datetime.timedelta(days=7)
        this_date_range_dict["end"] = start
        time_range.append(this_date_range_dict)
    return time_range

def shell_script(time_range, dump_json_raw):
    start_time_strftime = time_range['start'].strftime("%Y%m%d")
    end_time_strftime = time_range['end'].strftime("%Y%m%d")

    print "echo", echo_split_line_by_lrjust("[*] ", 1, 30, "+")
    print("echo `date`")
    print("echo range start from %s to %s")%(time_range['start'], time_range['end'])
    print("echo '%s' > %sto%s.json")%(dump_json_raw, start_time_strftime, end_time_strftime)
    print("/home/master/data/mongo_utils/mongodb-linux-x86_64-rhel70-3.4.1/bin/mongodump --host 10.8.8.111 --db eventsV4 --collection eventV4 --queryFile ./%sto%s.json")%(start_time_strftime, end_time_strftime)
    print("echo [*] dump completed %s to %s")%(start_time_strftime, end_time_strftime)
    print("mv ./dump ./%sto%s")%(start_time_strftime, end_time_strftime)
    print("rm ./%sto%s/eventsV4/*.json")%(start_time_strftime, end_time_strftime)
    print("/home/master/data/mongo_utils/mongodb-linux-x86_64-rhel70-3.4.1/bin/mongorestore --drop --db tmpBackendEvents --collection eventV4 ./%sto%s/eventsV4/eventV4.bson")%(start_time_strftime, end_time_strftime)
    print("echo [*] restore native data completed")
    print("/home/master/data/mongo_utils/mongodb-linux-x86_64-rhel70-3.4.1/bin/mongo tmpBackendEvents ./addApiTimeForBackendEvents.js")
    print("rm -rf ./%sto%s")%(start_time_strftime, end_time_strftime)
    print("/home/master/data/mongo_utils/mongodb-linux-x86_64-rhel70-3.4.1/bin/mongodump --db tmpBackendEvents --collection eventV4 --out ./%sto%s")%(start_time_strftime, end_time_strftime)
    print("mv ./%sto%s/tmpBackendEvents/eventV4.bson ./%sto%s/eventV4BackendEvents%sto%s.bson")%(start_time_strftime, end_time_strftime, start_time_strftime, end_time_strftime, start_time_strftime, end_time_strftime)
    print("rm -rf ./%sto%s/tmpBackendEvents/")%(start_time_strftime, end_time_strftime)
    print("mv *.json ./%sto%s/")%(start_time_strftime, end_time_strftime)
    print("echo `date`")
    print "echo", echo_split_line_by_lrjust("[*] ", 1, 30, "-")
    print("echo ''")


for time_range in time_range_gen(start, end):
    dump_json_raw = dump_json_gen(time_range)
    shell_script(time_range, dump_json_raw)
