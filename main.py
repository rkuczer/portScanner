import socket
import pyfiglet
import sys
from datetime import datetime

asciiBanner = pyfiglet.figlet_format("Port Scanner")
print(asciiBanner)

target = input(str("Target IP: "))


