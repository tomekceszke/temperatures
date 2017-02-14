#!/usr/bin/python

import os
import sys

# import rrdtool
import thingspeak
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from conf.settings import *
from conf.private_settings import *
from lib.common import *


class Sensor:
    def __init__(self):
        pass

    IN_LIVING_ROOM, IN_BEDROOM, OUT, POWER = range(4)


def check_temp(sensor, retry=False):
    if sensor == Sensor.IN_LIVING_ROOM:
        temp_result = read_temp_netcat(in_host, in_port)
    elif sensor == Sensor.IN_BEDROOM:
        temp_result = read_temp_get(bedroom_host)
    elif sensor == Sensor.OUT:
        temp_result = read_temp_local(out_path)
    elif sensor == Sensor.POWER:
        temp_result = read_temp_local(power_path)
    else:
        # temp_result = {'value': 'E', 'error': 'Unknown sensor'}
        sys.stderr.write("Unknown sensor\n")
        return

    value = temp_result['value']
    error = temp_result['error']

    if value == 'U':
        if retry:
            sys.stderr.write("Error " + sensor + ": " + error + "\n")
        else:
            sys.stderr.write("Repeat reading from sensor " + sensor + " reason: " + error + "\n")
            time.sleep(repeat_after_fail)
            value = check_temp(sensor, True)
    return value


def update_rrd_db(power_temp, in_temp, out_temp):
    data = 'N:' + str(power_temp) + ':' + str(in_temp) + ':' + str(out_temp)
    # print(data)
    # rrdtool.update(db_path, data)


def update_thingspeak_db(living_temp, bedroom_temp, out_temp, power_temp):
    living_temp_rounded = prepare_field(living_temp)
    bedroom_temp_rounded = prepare_field(bedroom_temp)
    out_temp_rounded = prepare_field(out_temp)
    power_temp_rounded = prepare_field(power_temp)

    ch = thingspeak.Channel(thingspeak_channel)
    response = ch.update({'api_key': thingspeak_write_api_key, 'field1': living_temp_rounded, 'field2': out_temp_rounded, 'field3': power_temp_rounded,
                          'field4': bedroom_temp_rounded})
    if response == "0":
        sys.stderr.write(
            "An error occured. Thingspeak won't be updated with values: living: %s, out %s, power: %s, bedroom: %s " % (
                living_temp_rounded, out_temp_rounded, power_temp_rounded, bedroom_temp_rounded))
        # else:
        #   print "Fields updated with values: living: %s, out %s, power: %s, bedroom: %s " % (
        #      living_temp_rounded, out_temp_rounded, power_temp_rounded, bedroom_temp_rounded)


def prepare_field(value):
    if not isinstance(value, float):
        sys.stderr.write("Value %s is not a float." % value)
        return "null"
    else:
        return round(value, 1)


def main():
    living_t = check_temp(Sensor.IN_LIVING_ROOM)
    bedroom_t = check_temp(Sensor.IN_BEDROOM)
    out_t = check_temp(Sensor.OUT)
    power_t = check_temp(Sensor.POWER)

    # print "bedroom temp:" + str(bedroom_t)
    # print "in temp:" + str(in_t)
    # print "power temp:" + str(power_t)

    # try:
    update_thingspeak_db(living_t, bedroom_t, out_t, power_t, )
    # except TypeError:
    # update_rrdb(power_t, in_t, out_t)


if __name__ == '__main__':
    main()
