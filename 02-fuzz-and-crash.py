#!/usr/bin/env python3

import socket
from base64 import decode,encode

# Target Information

RHOST = "192.168.226.166"   # IP of target Remote Host
RPORT = 31337   # Listening Port

# Build Response

buf = b""   # initialize bite-type object with empty string
buf += b"hhexme"    # message to send 
buf += b"\n"    # use \n to indicate end of "buf"

#Connect to target RHOST on RPORT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create IPV4 socket, TCP type
s.connect((RHOST,RPORT)) # connect to remote host on   port

# send response stored in "buf" to listening host
s.send(buf)

# print sent response to screen for our information

print(f"Response Sent: {buf.decode('utf-8')}") # base64 Decode with utf-8 to get string and print 

# Receive and store the response sent by target host. 1024 bytes

data = s.recv(1024)

# Print the received message

print(f"Received: {data.decode('utf-8')}") # base64 Decode to string and print
