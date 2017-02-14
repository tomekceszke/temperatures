#!/usr/bin/env python

import json
import cgi
import os
import sys
import urllib

sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from lib.common import *
from conf.settings import *


def send400(msg):
    print('Status: 400 ' + msg)
    print('Content-Type: application/json\n\n')
    exit()


form = cgi.FieldStorage()
sensor = form.getvalue('sensor')

if not sensor:
    send400('Missing Parameter')

result = ''
if sensor == 'in':
    result = read_temp_netcat(in_host, in_port)
    # result = {'value': urllib.urlopen('http://192.168.1.220/').read(), 'error': ''}
    # result = {'value': 'U', 'error': 'Unavailable'}

elif sensor == 'power':
    result = read_temp_local(power_path)
elif sensor == 'out':
    result = read_temp_local(out_path)
else:
    send400('Unknown Parameter')

print('Content-Type: application/json\n\n')
print(json.dumps(result))
