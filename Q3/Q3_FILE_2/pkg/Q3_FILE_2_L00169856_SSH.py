"""
# File             : Q3_FILE_2_L00169856_SSH.py
# Created          : 05/11/2021 21:11
# Author           : Patrick McGourty
# Version          : v1.0.0
# Licencing        : (c) 2021 Patrick McGourty
#                  Available under GNU public License (GPL)
# Description      : SSH script using paramiko
#

"""
import paramiko
"Importing paramiko making use of network tools"
"Creating a try statement with host keys/policy with the client information"
try:
    "Declaring session as a SSHClient"
    session = paramiko.SSHClient()
    "Loading host keys"
    session.load_system_host_keys()
    "Setting a policy for unknown host key"
    session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    "Calling information for SSH to find and login to the VM"
    session.connect(hostname="192.168.225.132", username="l00169856", password="GreatPassword", port=22)
    "Creating a while true statement saying while the above info is true continue with the try below"
    while True:
        try:
            "Declaring user_input as input and giving indication of how to continue"
            user_input = input("Enter text here or exit to close the application  ")
            "Making an if statement allowing the user to exit the try loop and close the session"
            if user_input == "exit":
                break
            "Reading standard in/out information sent to/back from the remote session"
            stdin, stdout, stderr = session.exec_command(user_input)
            "Converting/decoding the information received from the VM into a readable format"
            print(stdout.read().decode())
            "Using an except statement saying when when program is interrupted by the user to exit the try"
        except KeyboardInterrupt:
            break
    "Closing the session"
    session.close()
finally:
    "letting the user know the application has now been closed"
    print("Application Closed")
