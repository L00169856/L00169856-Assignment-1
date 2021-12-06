"""
# File             : Q4_FILE_2_PORTS.py
# Created          : 10/11/2021 18:01
# Author           : Patrick McGourty
# Version          : v1.0.0
# Licencing        : (c) 2021 Patrick McGourty
#                  Available under GNU public License (GPL)
# Description      : listing the open ports on the apache web server
#

"""
import socket
import re
"Importing the resoucres i need to make the code"
"Declaring ip and allowing it to be recognised as ipv4"
ip = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
"Declaring port_range and making it readable to scan"
port_range = re.compile("([0-9]+)-([0-9]+)")
"Declaring the min and max port values"
port_min = 0
port_max = 100

open_ports = []

while True:
    "Creating a while statement to allow the user to enter there ip"
    ip_entered = input("Enter the IP address here ")
    if ip.search(ip_entered):
        print("\n Valid IP")
        break

while True:
    "Creating a while statement allowing the user to enter the desired ports"
    port_ranges = input("Enter port range ")
    port_range_valid = port_range.search(port_ranges.replace(" ", ""))
    if port_range_valid:
        "Making sure the entered values equal the min and max"
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break
"Creating for statement to start scanning the ports"
for port in range(port_min, port_max + 1):

    try:
        "Creating a socket to connect to the ip address the user has entered"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            "scanning the entered ports for 0.5 seconds"
            s.settimeout(0.5)
            "connecting to the user entered ip and port number"
            s.connect((ip_entered, port))
            "allows for connection to a open port if previous was successful"
            open_ports.append(port)
    except:
        "Creating an except to catch closed ports"
        if port == 0:
            break
        else:
            print("port closed")

for port in open_ports:
    "Creating a for statement to show open port"
    print(f"port {port} is open on {ip_entered}, ")
    "Printing the port number and the ip entered"
    if port == 22:
        "Creating an if statement printing ssh open if port 22 is open"
        print("SSH is open")
    if port == 80:
        "Creating an if statement printing http open if port 80 is open"
        print("HTTP is open")
