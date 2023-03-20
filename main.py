import socket
import pyfiglet
import sys
from datetime import datetime

asciiBanner = pyfiglet.figlet_format("Port Scanner")
print(asciiBanner)

target = input(str("Target IP: "))

print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + str(datetime.now()))
print("_" * 50)

try:#Scan every port on target ip
    for port in range(1, 5000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        #Return open port
        result = s.connect_ex((target, port))
        if result == 0:
            print("[*] Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting ")
    sys.exit()
except socket.error:
    print("\ Host not responding")
    sys.exit()