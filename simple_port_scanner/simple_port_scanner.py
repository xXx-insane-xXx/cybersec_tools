#!/bin/python3

#Very basic port scanner. Can easily be broken.
#python3 scanner.py <ip>

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate hostname to ipv4 if not given an ipv4
else:
    print("Invalid amount of arguments.")
    print("Usage: python3 scanner.py <ip>")

#Add a banner
print("-" * 50)
print(f"Scanning target: {target}")
print(f"Time started: {datetime.now()}")

ports_opened = 0
ports_scanned = 0
try:
    for port in range(0, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1) #1s timeout
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open.")
            ports_opened += 1
        s.close()
        ports_scanned += 1

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Could not connect to the server.")
    sys.exit()


print("");
print(f"{ports_scanned} ports scanned", end=", ")
print(f"{ports_opened} ports opened", end=", ")
print(f"{ports_scanned - ports_opened} ports closed")
print("-" * 50)
