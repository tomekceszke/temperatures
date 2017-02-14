#!/bin/sh

mv temp.rrd temp.rrd.old &&
\
rrdtool create temp.rrd \
	--start N \
	--step 60 \
DS:power:GAUGE:120:15:90 \
DS:in:GAUGE:120:10:40 \
DS:out:GAUGE:120:-30:40 \
RRA:AVERAGE:0.5:1:43200 \
RRA:AVERAGE:0.5:60:8765 \
RRA:AVERAGE:0.5:10080:600 \
RRA:AVERAGE:0.5:43200:120

chmod 777 temp.rrd
