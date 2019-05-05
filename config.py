import socket

if socket.gethostname is "leon-pi-zero-1":
    dht22 = dht22 = [
        {
            "pin": 17,
            "name": "window_front"
        }
    ]

else if socket.gethostname is "leon-pi-zero-2":
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



influx_ip = "192.168.66.133"
influx_database = "smarthome"
influx_port = "8086"
