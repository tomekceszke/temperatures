#!/usr/bin/env python
import cgi

import os
# import tempfile
import sys

import rrdtool


sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))

from conf.settings import *


sensors = ['in', 'out', 'power']


def send400(msg):
    print('Status: 400 ' + msg)
    print('Content-Type: text/html\n\n')
    exit()


form = cgi.FieldStorage()

sensor = form.getvalue('sensor')
start = form.getvalue('start')
width = form.getvalue('width')
height = form.getvalue('height')

if not sensor or not start or not width or not height:
    send400('Missing Parameter')

if sensors.count(sensor) == 0:
    send400('Unknown Parameter')

# fd, path = tempfile.mkstemp('.png')

path = '/tmp/'+sensor+'-'+start+'-'+width+'-'+height+'.png'

rrdtool.graph(path,
              '--imgformat', 'PNG',
              '--width', width,
              '--height', height,
              '--start', '-' + start,
              # '--end', "-1",
              # '--vertical-label', 'Downloads/Day',
              # '--title', 'Annual downloads',
              # '--lower-limit', '0',
              # '--lazy',
              '--color', 'BACK#FFFFFF',
              '--border', '0',
              'DEF:' + sensor + '=' + db_path + ':' + sensor + ':AVERAGE',
              'LINE2:' + sensor + '#ff0000')

sys.stdout.write("Content-type: image/png\r\n\r\n")
sys.stdout.write(open(path, "rb").read())

