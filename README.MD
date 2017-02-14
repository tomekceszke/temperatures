# temperatures
Python based tool that collects data from ds18b20 (local or connected via esp8266) sensors.
Values are written to ThingSpeak.com (default) or local RRD database.
  
## Run
* create conf/private_settings.py according to [conf/private_settings_example.py](conf/private_settings_example.py) file with your own api key
* adapt [conf/settings.py](conf/settings.py) to your environment
* finally run [bin/temp.py](bin/temp.py) file to pool sensor and update thingspeak db

## Note
In [db/](db/) and [www/](www/) you will find files related to RRD database

## Technology stack
* python
* esp8266
* 1-wire
* ds18b20
* internet of things
* rrd



