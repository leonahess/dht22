import socket

dht22 = []

if socket.gethostname() == "leon-pi-zero-1":
    dht22 = [
        {
            "pin": 17,
            "name": "window_front"
        }
    ]

elif socket.gethostname() == "leon-pi-zero-2":
    dht22 = [
        {
            "pin": 17,
            "name": "window_back"
        },
        {
            "pin": 27,
            "name": "desk"
        }
    ]


influx_ip = "192.168.66.140"
influx_database = "smarthome"
influx_port = "8086"
influx_retention_policy = "2w"

'''
possible retention intervals:

ns	nanoseconds (1 billionth of a second)
u   microseconds (1 millionth of a second)
ms	milliseconds (1 thousandth of a second)
s	second
m	minute
h	hour
d	day
w	week
'''
