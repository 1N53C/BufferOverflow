#!/usr/bin/python

import socket
import sys

class colors:
    BANNER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def banner():
    print(colors.BANNER + "____ _______   .________________ _________   _______________ _______________________")
    print(colors.BANNER + "/_   |\      \  |   ____/\_____  \\_   ___ \   \_   _____/    |   \____    /\____    /")
    print(colors.BANNER + " |   |/   |   \ |____  \   _(__  </    \  \/   |    __) |    |   / /     /   /     /") 
    print(colors.BANNER + " |   /    |    \/       \ /       \     \____  |     \  |    |  / /     /_  /     /_ ")
    print(colors.BANNER + " |___\____|__  /______  //______  /\______  /  \___  /  |______/ /_______ \/_______ \\")
    print(colors.BANNER + "             \/       \/        \/        \/       \/                    \/        \/" + colors.ENDC)
    print(colors.WARNING +"*****************************  Fuzzer by invasive-security.de  *********************** " + colors.ENDC)

def usage():
    print(colors.OKGREEN + "USAGE: ./insecfuzzer.py <ip> <port>" + colors.ENDC)
    print(colors.OKGREEN + "Example: ./insecfuzzer.py 127.0.0.1 21" + colors.ENDC)

banner()
usage()

# implement argv host, port, bufferlength
host = str(sys.argv[1]) 
port = sys.argv[2]         

print(host)
print port

buffer = ['\x41'] 
buffer_length = 100

'''
while len(buffer) <= 30:
    buffer.append('\x41' * buffer_length)
    buffer_length = buffer_length + 200
    print("Buffer: " + str(buffer_length) + "\r\n")
    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(1024)
s.send(buffer)
data = s.recv(1024)
'''