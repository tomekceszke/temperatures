#!/usr/bin/rrdcgi 
<HTML>
 <HEAD><TITLE>Heating</TITLE></HEAD>
 <BODY>
 <RRD::GRAPH www/temp_power_short.png  --imginfo '<IMG SRC=/%s WIDTH=%lu HEIGHT=%lu >'  -N -E --lazy -s -3h  -w 1300 -h 150 --title="3h" -v "heating [C]" --right-axis 1:0
        DEF:power=db/temp.rrd:power:AVERAGE
	LINE2:power#ff0000:heating
	GPRINT:power:LAST:" [%2.2lf%sC]"
	>
&nbsp;
&nbsp;
<RRD::GRAPH www/temp_all_24.png  --imginfo '<IMG SRC=/%s WIDTH=%lu HEIGHT=%lu >' -N -E --lazy -s -24h  -w 1300 -h 150  --title="24h" -v "temperature [C]" --right-axis 1:0
        DEF:power=db/temp.rrd:power:AVERAGE
        DEF:in=db/temp.rrd:in:AVERAGE
        DEF:out=db/temp.rrd:out:AVERAGE
        LINE2:power#ff0000:zasilanie
	GPRINT:power:LAST:"%2.2lf%sC\t"
        LINE2:in#2e2efe:wewnatrz
	GPRINT:in:LAST:"%2.2lf%sC\t"
        LINE2:out#00a000:zewnatrz
	GPRINT:out:LAST:"%2.2lf%sC"
        >
&nbsp;
 <RRD::GRAPH www/temp_in_out_long.png  --imginfo '<IMG SRC=/%s WIDTH=%lu HEIGHT=%lu >'  -N -E --lazy -s -7d  -w 1300 -h 150  --title="week" -v "temperature [C]"  --right-axis 1:0
        DEF:in=db/temp.rrd:in:AVERAGE
	DEF:out=db/temp.rrd:out:AVERAGE
	AREA:in#2e2efe:"wewnatrz"
        GPRINT:in:LAST:"%2.2lf%sC\t"
    	AREA:out#00a000:"zewnatrz"
        GPRINT:out:LAST:"%2.2lf%sC"
	>
&nbsp;

 </BODY>
 </HTML>
