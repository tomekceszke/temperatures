thingspeak_channel = '107384'
base_dir = '/sys/bus/w1/devices/'
device_file = '/w1_slave'
repeat_after_fail = 20  # seconds
db_path = 'temperatures/db/temp.rrd'  # optionally
power_id = '28-00000504c528'
out_id = '28-0000057b9502'
# in_id = '28-041469f284ff'
in_host = '192.168.11.11'
in_port = 4444
bedroom_host = '192.168.11.240'

out_path = base_dir + out_id + device_file
power_path = base_dir + power_id + device_file
