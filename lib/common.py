#!/usr/bin/python
import socket
import urllib

__author__ = "Tomasz Ceszke"


def read_temp_netcat(hostname, port):
    try:
        out = netcat(hostname, port)
    except socket.error:
        return parse_temp(None, "SOCKET PROBLEM")

    lines = out.splitlines()
    # print "Remote temp output:", out
    # print("split: "+str(lines))
    return parse_temp(lines)


def read_temp_get(hostname):
    try:
        temp = urllib.urlopen('http://' + hostname).read()
    except IOError:
        return {'value': 'U', 'error': 'IOError'}

    temp_f = float(temp.strip())
    if temp_f != 85.0:
        return {'value': temp_f, 'error': ''}
    else:
        return {'value': 'U', 'error': '85.0'}


def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    data = s.recv(1024)
    s.close()
    return data


def read_temp_local(path):
    try:
        f = open(path, 'r')
    except IOError:
        return {'value': 'U', 'error': 'IOError'}
    lines = f.readlines()
    f.close()
    return parse_temp(lines)


def parse_temp(data, reason='EMPTY DATA'):
    if data:
        if data[0].strip()[-3:] == 'YES':
            equals_pos = data[1].find('t=')
            if equals_pos != -1:
                temp_string = data[1][equals_pos + 2:]
                temp_c = float(temp_string) / 1000.0
                if temp_c != 85.0:
                    return {'value': temp_c, 'error': ''}
                else:
                    reason = '85.0'
            else:
                reason = "MISSING T"
        else:
            reason = 'CRC'
    return {'value': 'U', 'error': reason}
