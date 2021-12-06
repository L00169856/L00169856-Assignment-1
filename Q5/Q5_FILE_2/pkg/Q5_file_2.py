"""
# File             : Q5_file_2.py
# Created          : 15/11/2021 19:33
# Author           : Patrick McGourty
# Version          : v1.0.0
# Licencing        : (c) 2021 Patrick McGourty
#                  Available under GNU public License (GPL)
# Description      : Creating a directory structure Labs with sub-folders lab1 and lab2
#

"""
import os
import time
"Importing the modules needed"
path = "D:/Labs/Lab1"
"Declaring path and where to created the folder"
path1 = "D:/Labs/Lab2"
"Declaring path1 and where to make the folders"
try:
    "Creating a try statement to created the folders using the declared variable's"
    os.makedirs(path)
    "Using making directory to create the folders in the specified point for both path and path1"
    os.makedirs(path1)
    print("Folder created")
    "Alerting the user that the folder has been created"
except FileExistsError:
    "Using an except statement to not make duplicates of the folder if it already exists"
    print("File already exists")
    "Alerting the user that the file already exists"
